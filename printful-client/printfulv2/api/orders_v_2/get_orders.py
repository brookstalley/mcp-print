from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_orders_response_200 import GetOrdersResponse200
from ...models.get_orders_response_401 import GetOrdersResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/orders",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetOrdersResponse200, GetOrdersResponse401]]:
    if response.status_code == 200:
        response_200 = GetOrdersResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetOrdersResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetOrdersResponse200, GetOrdersResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetOrdersResponse200, GetOrdersResponse401]]:
    """Retrieve a list of orders

     Retrieve a list of orders from a specific store. The order list will be paginated with twenty items
    per page by default.

    Args:
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOrdersResponse200, GetOrdersResponse401]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetOrdersResponse200, GetOrdersResponse401]]:
    """Retrieve a list of orders

     Retrieve a list of orders from a specific store. The order list will be paginated with twenty items
    per page by default.

    Args:
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOrdersResponse200, GetOrdersResponse401]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetOrdersResponse200, GetOrdersResponse401]]:
    """Retrieve a list of orders

     Retrieve a list of orders from a specific store. The order list will be paginated with twenty items
    per page by default.

    Args:
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOrdersResponse200, GetOrdersResponse401]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetOrdersResponse200, GetOrdersResponse401]]:
    """Retrieve a list of orders

     Retrieve a list of orders from a specific store. The order list will be paginated with twenty items
    per page by default.

    Args:
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOrdersResponse200, GetOrdersResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
