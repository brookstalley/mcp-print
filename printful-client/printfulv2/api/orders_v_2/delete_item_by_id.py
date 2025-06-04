from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_item_by_id_response_400 import DeleteItemByIdResponse400
from ...models.delete_item_by_id_response_401 import DeleteItemByIdResponse401
from ...models.delete_item_by_id_response_403 import DeleteItemByIdResponse403
from ...models.delete_item_by_id_response_404 import DeleteItemByIdResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: Union[int, str],
    order_item_id: Union[int, str],
    *,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/v2/orders/{order_id}/order-items/{order_item_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404
    ]
]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = DeleteItemByIdResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = DeleteItemByIdResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = DeleteItemByIdResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = DeleteItemByIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404
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
    order_item_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404
    ]
]:
    """Delete Order Item

     Remove a single item from the order.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        order_item_id=order_item_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: Union[int, str],
    order_item_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404
    ]
]:
    """Delete Order Item

     Remove a single item from the order.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404]
    """

    return sync_detailed(
        order_id=order_id,
        order_item_id=order_item_id,
        client=client,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    order_id: Union[int, str],
    order_item_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404
    ]
]:
    """Delete Order Item

     Remove a single item from the order.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        order_item_id=order_item_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: Union[int, str],
    order_item_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404
    ]
]:
    """Delete Order Item

     Remove a single item from the order.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteItemByIdResponse400, DeleteItemByIdResponse401, DeleteItemByIdResponse403, DeleteItemByIdResponse404]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            order_item_id=order_item_id,
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
