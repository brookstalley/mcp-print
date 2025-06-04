from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_webhooks_response_200 import GetWebhooksResponse200
from ...models.get_webhooks_response_401 import GetWebhooksResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    params: dict[str, Any] = {}

    params["show_expired"] = show_expired

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/webhooks",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetWebhooksResponse200, GetWebhooksResponse401]]:
    if response.status_code == 200:
        response_200 = GetWebhooksResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetWebhooksResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetWebhooksResponse200, GetWebhooksResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetWebhooksResponse200, GetWebhooksResponse401]]:
    """Get webhook configuration

     Returns a configured webhook URL and a list of webhook event types enabled for the store

    Args:
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWebhooksResponse200, GetWebhooksResponse401]]
    """

    kwargs = _get_kwargs(
        show_expired=show_expired,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetWebhooksResponse200, GetWebhooksResponse401]]:
    """Get webhook configuration

     Returns a configured webhook URL and a list of webhook event types enabled for the store

    Args:
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWebhooksResponse200, GetWebhooksResponse401]
    """

    return sync_detailed(
        client=client,
        show_expired=show_expired,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetWebhooksResponse200, GetWebhooksResponse401]]:
    """Get webhook configuration

     Returns a configured webhook URL and a list of webhook event types enabled for the store

    Args:
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWebhooksResponse200, GetWebhooksResponse401]]
    """

    kwargs = _get_kwargs(
        show_expired=show_expired,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetWebhooksResponse200, GetWebhooksResponse401]]:
    """Get webhook configuration

     Returns a configured webhook URL and a list of webhook event types enabled for the store

    Args:
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWebhooksResponse200, GetWebhooksResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
            show_expired=show_expired,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
