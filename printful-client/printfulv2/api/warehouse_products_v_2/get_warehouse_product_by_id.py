from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_warehouse_product_by_id_response_200 import GetWarehouseProductByIdResponse200
from ...models.get_warehouse_product_by_id_response_401 import GetWarehouseProductByIdResponse401
from ...models.get_warehouse_product_by_id_response_404 import GetWarehouseProductByIdResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    warehouse_product_id: int,
    *,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/warehouse-products/{warehouse_product_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
]:
    if response.status_code == 200:
        response_200 = GetWarehouseProductByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetWarehouseProductByIdResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = GetWarehouseProductByIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    warehouse_product_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
]:
    """Retrieve a single warehouse product

     Get information about a single warehouse product with it's stock location.

    Args:
        warehouse_product_id (int):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]]
    """

    kwargs = _get_kwargs(
        warehouse_product_id=warehouse_product_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    warehouse_product_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
]:
    """Retrieve a single warehouse product

     Get information about a single warehouse product with it's stock location.

    Args:
        warehouse_product_id (int):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
    """

    return sync_detailed(
        warehouse_product_id=warehouse_product_id,
        client=client,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    warehouse_product_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
]:
    """Retrieve a single warehouse product

     Get information about a single warehouse product with it's stock location.

    Args:
        warehouse_product_id (int):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]]
    """

    kwargs = _get_kwargs(
        warehouse_product_id=warehouse_product_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    warehouse_product_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
]:
    """Retrieve a single warehouse product

     Get information about a single warehouse product with it's stock location.

    Args:
        warehouse_product_id (int):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetWarehouseProductByIdResponse200, GetWarehouseProductByIdResponse401, GetWarehouseProductByIdResponse404]
    """

    return (
        await asyncio_detailed(
            warehouse_product_id=warehouse_product_id,
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
