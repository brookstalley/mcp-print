from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.disable_webhook_response_401 import DisableWebhookResponse401
from ...models.disable_webhook_response_404 import DisableWebhookResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v2/webhooks",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 401:
        response_401 = DisableWebhookResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = DisableWebhookResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]:
    """Disable webhook support

     Removes the webhook URL and all event types from the store.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]
    """

    kwargs = _get_kwargs(
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]:
    """Disable webhook support

     Removes the webhook URL and all event types from the store.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]
    """

    return sync_detailed(
        client=client,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]:
    """Disable webhook support

     Removes the webhook URL and all event types from the store.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]
    """

    kwargs = _get_kwargs(
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]]:
    """Disable webhook support

     Removes the webhook URL and all event types from the store.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DisableWebhookResponse401, DisableWebhookResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
