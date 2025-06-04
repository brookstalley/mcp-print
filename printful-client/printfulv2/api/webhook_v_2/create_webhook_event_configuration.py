from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.catalog_stock_updated_event_configuration import CatalogStockUpdatedEventConfiguration
from ...models.create_webhook_event_configuration_response_200 import CreateWebhookEventConfigurationResponse200
from ...models.create_webhook_event_configuration_response_400 import CreateWebhookEventConfigurationResponse400
from ...models.create_webhook_event_configuration_response_401 import CreateWebhookEventConfigurationResponse401
from ...models.default_event_configuration import DefaultEventConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    event_type: str,
    *,
    body: Union["CatalogStockUpdatedEventConfiguration", "DefaultEventConfiguration"],
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/v2/webhooks/{event_type}",
    }

    _body: dict[str, Any]
    if isinstance(body, DefaultEventConfiguration):
        _body = body.to_dict()
    else:
        _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateWebhookEventConfigurationResponse200,
        CreateWebhookEventConfigurationResponse400,
        CreateWebhookEventConfigurationResponse401,
    ]
]:
    if response.status_code == 200:
        response_200 = CreateWebhookEventConfigurationResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CreateWebhookEventConfigurationResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateWebhookEventConfigurationResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateWebhookEventConfigurationResponse200,
        CreateWebhookEventConfigurationResponse400,
        CreateWebhookEventConfigurationResponse401,
    ]
]:
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
    body: Union["CatalogStockUpdatedEventConfiguration", "DefaultEventConfiguration"],
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        CreateWebhookEventConfigurationResponse200,
        CreateWebhookEventConfigurationResponse400,
        CreateWebhookEventConfigurationResponse401,
    ]
]:
    """Set up event configuration

     Use this endpoint to create or replace specific event configuration for a store.

    Setting up the [Catalog stock updated](#operation/catalogStockUpdated) webhook requires passing
    products (currently only IDs are taken into account).

    Stock update webhook will only include information for the products specified in the `products`
    param.

    Args:
        event_type (str):
        x_pf_store_id (Union[Unset, str]):
        body (Union['CatalogStockUpdatedEventConfiguration', 'DefaultEventConfiguration']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWebhookEventConfigurationResponse200, CreateWebhookEventConfigurationResponse400, CreateWebhookEventConfigurationResponse401]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        body=body,
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
    body: Union["CatalogStockUpdatedEventConfiguration", "DefaultEventConfiguration"],
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        CreateWebhookEventConfigurationResponse200,
        CreateWebhookEventConfigurationResponse400,
        CreateWebhookEventConfigurationResponse401,
    ]
]:
    """Set up event configuration

     Use this endpoint to create or replace specific event configuration for a store.

    Setting up the [Catalog stock updated](#operation/catalogStockUpdated) webhook requires passing
    products (currently only IDs are taken into account).

    Stock update webhook will only include information for the products specified in the `products`
    param.

    Args:
        event_type (str):
        x_pf_store_id (Union[Unset, str]):
        body (Union['CatalogStockUpdatedEventConfiguration', 'DefaultEventConfiguration']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWebhookEventConfigurationResponse200, CreateWebhookEventConfigurationResponse400, CreateWebhookEventConfigurationResponse401]
    """

    return sync_detailed(
        event_type=event_type,
        client=client,
        body=body,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    event_type: str,
    *,
    client: AuthenticatedClient,
    body: Union["CatalogStockUpdatedEventConfiguration", "DefaultEventConfiguration"],
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        CreateWebhookEventConfigurationResponse200,
        CreateWebhookEventConfigurationResponse400,
        CreateWebhookEventConfigurationResponse401,
    ]
]:
    """Set up event configuration

     Use this endpoint to create or replace specific event configuration for a store.

    Setting up the [Catalog stock updated](#operation/catalogStockUpdated) webhook requires passing
    products (currently only IDs are taken into account).

    Stock update webhook will only include information for the products specified in the `products`
    param.

    Args:
        event_type (str):
        x_pf_store_id (Union[Unset, str]):
        body (Union['CatalogStockUpdatedEventConfiguration', 'DefaultEventConfiguration']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWebhookEventConfigurationResponse200, CreateWebhookEventConfigurationResponse400, CreateWebhookEventConfigurationResponse401]]
    """

    kwargs = _get_kwargs(
        event_type=event_type,
        body=body,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    event_type: str,
    *,
    client: AuthenticatedClient,
    body: Union["CatalogStockUpdatedEventConfiguration", "DefaultEventConfiguration"],
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        CreateWebhookEventConfigurationResponse200,
        CreateWebhookEventConfigurationResponse400,
        CreateWebhookEventConfigurationResponse401,
    ]
]:
    """Set up event configuration

     Use this endpoint to create or replace specific event configuration for a store.

    Setting up the [Catalog stock updated](#operation/catalogStockUpdated) webhook requires passing
    products (currently only IDs are taken into account).

    Stock update webhook will only include information for the products specified in the `products`
    param.

    Args:
        event_type (str):
        x_pf_store_id (Union[Unset, str]):
        body (Union['CatalogStockUpdatedEventConfiguration', 'DefaultEventConfiguration']):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWebhookEventConfigurationResponse200, CreateWebhookEventConfigurationResponse400, CreateWebhookEventConfigurationResponse401]
    """

    return (
        await asyncio_detailed(
            event_type=event_type,
            client=client,
            body=body,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
