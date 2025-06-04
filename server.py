#!/usr/bin/env python3
"""
Printful → MCP bridge (SSE transport, sync client, per‑client quotas)

Env
---
PRINTFUL_API_KEY   – https://developers.printful.com
AUTH_TOKEN         – Bearer token for *client 1*
PORT               – optional (default 8000)

FastMCP ≥ 2.3.2 required (for http_app()).
"""

from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env.dev", override=False)

import inspect
import os
import pkgutil
import time
from datetime import datetime, timedelta, timezone
from importlib import import_module
from typing import Any, Dict, Literal, TypedDict

from fastapi import Depends, FastAPI, Header, HTTPException, Request, status
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import PlainTextResponse
from fastmcp import FastMCP
from sse_starlette import ServerSentEvent as SseEvent           # ≥ v2 API
import printfulv2                                               # installed package
from printfulv2 import AuthenticatedClient

import logging

# ──────────────── Utilities ────────────────────────────
def bearer_token_from_header(header: str) -> str:
    """Extract the bearer token from an Authorization header."""
    print(f"Authorization header: {header}")
    if not header.startswith("Bearer "):
        return header.strip()
    return header.removeprefix("Bearer ").strip()

# ──────────────── per‑client policy store ─────────────────────
class ClientPolicy(TypedDict):
    id: int
    create_draft_order: bool
    place_order: bool
    cancel_order: bool
    daily_limit: float
    spent_today: float
    reset_at: float

def _midnight_utc_epoch() -> float:
    now = datetime.now(timezone.utc)
    nxt = (now + timedelta(days=1)).replace(hour=0, minute=0,
                                           second=0, microsecond=0)
    return nxt.timestamp()

_CLIENTS: Dict[str, ClientPolicy] = {
    os.getenv("AUTH_TOKEN", ""): {
        "id": 1,
        "create_draft_order": True,
        "place_order": True,
        "cancel_order": True,
        "daily_limit": 50.0,
        "spent_today": 0.0,
        "reset_at": _midnight_utc_epoch(),
    }
}

_BEARER_TOKENS = {tok for tok in _CLIENTS}  # for quick lookup
print(f"Bearer tokens: {_BEARER_TOKENS}")
# Map Printful operationIds → permission flags
_OP_PERM: Dict[str, Literal[
    "create_draft_order", "place_order", "cancel_order"
]] = {
    "postOrdersDraft":  "create_draft_order",
    "postOrders":       "place_order",
    "deleteOrdersById": "cancel_order",
}

# ─────────────── client lookup / quota helper ────────────────
def get_client(request: Request,
               Authorization: str = Header(...)) -> ClientPolicy:  # noqa: D401
    token = Authorization.removeprefix("Bearer ").strip()
    logger = logging.getLogger(__name__)
    logger.info(f"Client token: {token}")
    client = _CLIENTS.get(token)
    if not client:
        print(f"Invalid client token: {token}")
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            "invalid bearer token 🦛")

    # daily roll‑over
    if time.time() >= client["reset_at"]:
        client["spent_today"] = 0.0
        client["reset_at"] = _midnight_utc_epoch()
    request.state.client = client
    return client

# ──────────────── Printful sync client ───────────────────────
PRINTFUL = AuthenticatedClient(
    base_url="https://api.printful.com",
    token=os.environ["PRINTFUL_API_KEY"],
    timeout=30.0,
    follow_redirects=True,
)

# ─────────────── dynamic operation dispatcher ────────────────
class PrintfulInvoker:
    def __init__(self) -> None:
        api_pkg = import_module("printfulv2.api")
        funcs: Dict[str, Any] = {}
        for _, mod_name, _ in pkgutil.walk_packages(api_pkg.__path__,
                                                    api_pkg.__name__ + "."):
            mod = import_module(mod_name)
            for name, obj in inspect.getmembers(mod, callable):
                if name.endswith("_sync"):
                    op_id = getattr(obj, "__operation_id__", name[:-5])
                    funcs[op_id] = obj
        self._funcs = funcs

    async def __call__(self, operation_id: str,
                       params: Dict[str, Any],
                       client: ClientPolicy) -> Any:
        func = self._funcs.get(operation_id)
        if not func:
            raise HTTPException(404, f"Unknown Printful op '{operation_id}'")

        # permission check
        flag = _OP_PERM.get(operation_id)
        if flag and not client[flag]:
            raise HTTPException(status.HTTP_403_FORBIDDEN,
                                f"Client lacks permission: {flag}")

        # naïve cost gate (caller passes order_total)
        cost = float(params.pop("order_total", 0.0))
        if flag == "place_order" and cost:
            if client["spent_today"] + cost > client["daily_limit"]:
                raise HTTPException(status.HTTP_402_PAYMENT_REQUIRED,
                                    "Daily spend limit exceeded 🦛")
            client["spent_today"] += cost

        return await run_in_threadpool(func, client=PRINTFUL, **params)

printful_call = PrintfulInvoker()

# ─────────────── FastMCP tooling definition ──────────────────
mcp = FastMCP("Printful‑MCP‑Bridge")

@mcp.tool()
async def call_printful(operation_id: str,
                        params: Dict[str, Any] = {},
                        client: ClientPolicy = Depends(get_client)) -> Any:  # noqa: D401
    """Invoke any Printful endpoint by its `operationId` (quota‑aware)."""
    return await printful_call(operation_id, params, client)

# ─────────────── FastAPI / Starlette wrapper ─────────────────
app: FastAPI = mcp.http_app(transport="sse")   # FastMCP ≥ 2.3.2

@app.middleware("http")
async def auth_guard(request: Request, call_next):
    """Return 401 without crashing when bearer token is invalid."""
    client_token = bearer_token_from_header(request.headers.get("authorization", ""))
    logger = logging.getLogger()
    logger.info(f"Client token: {client_token}")   
    
    print(f"Client token: {client_token}") 
    if client_token not in _BEARER_TOKENS:
        return PlainTextResponse(f"invalid bearer token {client_token}", status_code=401)
    return await call_next(request)

# ─────────────── run via uvicorn ─────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0",
                port=int(os.getenv("PORT", "8000")))
