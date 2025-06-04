from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_items_by_order_id_response_400 import GetItemsByOrderIdResponse400
from ...models.get_items_by_order_id_response_401 import GetItemsByOrderIdResponse401
from ...models.get_items_by_order_id_response_403 import GetItemsByOrderIdResponse403
from ...models.get_items_by_order_id_response_404 import GetItemsByOrderIdResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: Union[int, str],
    *,
    type_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    params: dict[str, Any] = {}

    params["type"] = type_

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/orders/{order_id}/order-items",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetItemsByOrderIdResponse400,
        GetItemsByOrderIdResponse401,
        GetItemsByOrderIdResponse403,
        GetItemsByOrderIdResponse404,
    ]
]:
    if response.status_code == 400:
        response_400 = GetItemsByOrderIdResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetItemsByOrderIdResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GetItemsByOrderIdResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = GetItemsByOrderIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetItemsByOrderIdResponse400,
        GetItemsByOrderIdResponse401,
        GetItemsByOrderIdResponse403,
        GetItemsByOrderIdResponse404,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        GetItemsByOrderIdResponse400,
        GetItemsByOrderIdResponse401,
        GetItemsByOrderIdResponse403,
        GetItemsByOrderIdResponse404,
    ]
]:
    """Retrieve a list of order items

     This endpoint retrieves the list of items that belong to the order.

    Args:
        order_id (Union[int, str]):
        type_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetItemsByOrderIdResponse400, GetItemsByOrderIdResponse401, GetItemsByOrderIdResponse403, GetItemsByOrderIdResponse404]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        type_=type_,
        limit=limit,
        offset=offset,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        GetItemsByOrderIdResponse400,
        GetItemsByOrderIdResponse401,
        GetItemsByOrderIdResponse403,
        GetItemsByOrderIdResponse404,
    ]
]:
    """Retrieve a list of order items

     This endpoint retrieves the list of items that belong to the order.

    Args:
        order_id (Union[int, str]):
        type_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetItemsByOrderIdResponse400, GetItemsByOrderIdResponse401, GetItemsByOrderIdResponse403, GetItemsByOrderIdResponse404]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        type_=type_,
        limit=limit,
        offset=offset,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        GetItemsByOrderIdResponse400,
        GetItemsByOrderIdResponse401,
        GetItemsByOrderIdResponse403,
        GetItemsByOrderIdResponse404,
    ]
]:
    """Retrieve a list of order items

     This endpoint retrieves the list of items that belong to the order.

    Args:
        order_id (Union[int, str]):
        type_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetItemsByOrderIdResponse400, GetItemsByOrderIdResponse401, GetItemsByOrderIdResponse403, GetItemsByOrderIdResponse404]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        type_=type_,
        limit=limit,
        offset=offset,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    type_: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        GetItemsByOrderIdResponse400,
        GetItemsByOrderIdResponse401,
        GetItemsByOrderIdResponse403,
        GetItemsByOrderIdResponse404,
    ]
]:
    """Retrieve a list of order items

     This endpoint retrieves the list of items that belong to the order.

    Args:
        order_id (Union[int, str]):
        type_ (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetItemsByOrderIdResponse400, GetItemsByOrderIdResponse401, GetItemsByOrderIdResponse403, GetItemsByOrderIdResponse404]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            type_=type_,
            limit=limit,
            offset=offset,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
