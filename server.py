#!/usr/bin/env python3
"""
Printful → MCP bridge (OpenAPI‑driven, per‑client quotas)
=======================================================

* Auto‑generates **all** Printful tools from `printful_apiv2_openapi.json`.
* Preserves the existing bearer‑token client map and quota logic.
* Applies auth / daily‑spend / permission checks to every generated tool.

Test with:
```bash
export PRINTFUL_API_KEY=…  # and AUTH_TOKEN=… in .env.dev or env
python server.py
curl -X POST http://localhost:8000/tools/list-printful-tools -H "Authorization: Bearer $AUTH_TOKEN"
```
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Literal, TypedDict

import httpx
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Header, HTTPException, Request
from fastapi.responses import PlainTextResponse
from fastmcp import FastMCP

# ─────────────── env / secrets ──────────────────────────

load_dotenv(Path(__file__).parent / ".env.dev", override=True)

PRINTFUL_API_KEY = os.environ["PRINTFUL_API_KEY"]

# ─────────────── bearer‑token client DB ─────────────────

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
    nxt = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
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

_BEARER_TOKENS = {tok for tok in _CLIENTS if tok}

# Map Printful operationIds → permission flags
_OP_PERM: Dict[str, Literal["create_draft_order", "place_order", "cancel_order"]] = {
    "postOrdersDraft": "create_draft_order",
    "postOrders": "place_order",
    "deleteOrdersById": "cancel_order",
}

# ─────────────── auth / quota dependency ────────────────

def bearer_token_from_header(hdr: str | None) -> str:
    if not hdr:
        return ""
    return hdr.removeprefix("Bearer ").strip()


def get_client(request: Request, Authorization: str = Header(...)) -> ClientPolicy:  # noqa: D401
    token = bearer_token_from_header(Authorization)
    client = _CLIENTS.get(token)
    if not client:
        raise HTTPException(401, "invalid bearer token 🦛")

    # midnight rollover
    if time.time() >= client["reset_at"]:
        client["spent_today"] = 0.0
        client["reset_at"] = _midnight_utc_epoch()

    request.state.client = client
    return client

# ─────────────── OpenAPI‑driven MCP build ──────────────

spec_path = Path(__file__).parent / "printful_apiv2_openapi.json"
openapi_spec: Dict[str, Any] = json.loads(spec_path.read_text())

# Ensure Printful auth headers survive any FastMCP injection
async def _ensure_printful_auth(request: httpx.Request):
    request.headers["Authorization"] = f"Bearer {PRINTFUL_API_KEY}"
    request.headers["X-Auth-Token"] = PRINTFUL_API_KEY

api_client = httpx.AsyncClient(
    base_url="https://api.printful.com",
    timeout=30.0,
    event_hooks={"request": [_ensure_printful_auth]},
)

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=api_client,
    name="Printful‑MCP‑Bridge",
    transport="streamable-http",
    security_defaults={"bearerAuth": PRINTFUL_API_KEY},
)

# ─────────────── helper: iterate tools ────────────────

def _iter_tools(m) -> Iterable[Any]:
    if hasattr(m, "tools"):
        return m.tools.values()  # type: ignore[attr-defined]
    if hasattr(m, "_tools"):
        return m._tools.values()  # type: ignore[attr-defined]
    if hasattr(m, "list_tools") and hasattr(m, "tool"):
        return (m.tool(n) for n in m.list_tools())  # type: ignore[attr-defined]
    return []

# ───── post‑generation hook: auth, quota & prompt ─────

for tool in _iter_tools(mcp):
    original_fn = tool.fn

    async def wrapped_fn(*args, __orig=original_fn, **kwargs):  # type: ignore[name-defined]
        request: Request = kwargs.get("request")
        client: ClientPolicy = request.state.client

        op_id = tool.metadata.get("operationId", tool.name)
        perm_flag = _OP_PERM.get(op_id)
        if perm_flag and not client[perm_flag]:
            raise HTTPException(403, f"Client lacks permission: {perm_flag}")

        body = kwargs.get("body") or {}
        cost = float(body.pop("order_total", 0.0)) if isinstance(body, dict) else 0.0
        if perm_flag == "place_order" and cost:
            if client["spent_today"] + cost > client["daily_limit"]:
                raise HTTPException(402, "Daily spend limit exceeded 🦛")
            client["spent_today"] += cost

        return await __orig(*args, **kwargs)

    tool.fn = wrapped_fn  # type: ignore[assignment]
    tool.dependencies.append(Depends(get_client))

    # Prompt injection (fixed string literals)
    op_id = tool.metadata.get("operationId", tool.name)
    summary = tool.metadata.get("summary") or tool.metadata.get("description") or "Printful API call"
    tool.prompt = (
        f"**Printful {op_id}**\n\n"
        f"{summary.strip()}\n\n"
        "Provide parameters exactly as defined by the Printful OpenAPI schema."
    )

# ─────────────── FastAPI wrapper ────────────────────────

app: FastAPI = mcp.http_app()

@app.middleware("http")
async def auth_guard(request: Request, call_next):
    token = bearer_token_from_header(request.headers.get("authorization"))
    if token not in _BEARER_TOKENS:
        return PlainTextResponse("invalid bearer token", status_code=401)
    return await call_next(request)

# ─────────────── run via uvicorn ─────────────────────────

if __name__ == "__main__":
    import uvicorn

    sample = [r for r in app.routes if r.path.startswith("/tools")]
    print("Generated tool endpoints (first 5):")
    for r in sample[:5]:
        print(" •", r.path)

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
