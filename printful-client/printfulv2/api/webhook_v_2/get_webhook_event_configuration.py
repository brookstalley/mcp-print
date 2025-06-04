from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_webhook_event_configuration_response_200 import GetWebhookEventConfigurationResponse200
from ...models.get_webhook_event_configuration_response_401 import GetWebhookEventConfigurationResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_type: str,
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
        "url": f"/v2/webhooks/{event_type}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]:
    if response.status_code == 200:
        response_200 = GetWebhookEventConfigurationResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetWebhookEventConfigurationResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    event_type: str,
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]:
    """Get event configuration

     Returns event configuration for store

    Args:
        event_type (str):
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        show_expired=show_expired,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    event_type: str,
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]:
    """Get event configuration

     Returns event configuration for store

    Args:
        event_type (str):
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]
    """

    return sync_detailed(
        event_type=event_type,
        client=client,
        show_expired=show_expired,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    event_type: str,
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]:
    """Get event configuration

     Returns event configuration for store

    Args:
        event_type (str):
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        show_expired=show_expired,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_type: str,
    *,
    client: AuthenticatedClient,
    show_expired: Union[Unset, bool] = UNSET,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]]:
    """Get event configuration

     Returns event configuration for store

    Args:
        event_type (str):
        show_expired (Union[Unset, bool]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWebhookEventConfigurationResponse200, GetWebhookEventConfigurationResponse401]
    """

    return (
        await asyncio_detailed(
            event_type=event_type,
            client=client,
            show_expired=show_expired,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
