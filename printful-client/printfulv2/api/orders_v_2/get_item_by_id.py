from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_item_by_id_response_401 import GetItemByIdResponse401
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
        "method": "get",
        "url": f"/v2/orders/{order_id}/order-items/{order_item_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetItemByIdResponse401]:
    if response.status_code == 401:
        response_401 = GetItemByIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetItemByIdResponse401]:
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
) -> Response[GetItemByIdResponse401]:
    """Retrieve a single order item

     This endpoint will retrieve a single order item specified in the request.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetItemByIdResponse401]
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
) -> Optional[GetItemByIdResponse401]:
    """Retrieve a single order item

     This endpoint will retrieve a single order item specified in the request.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetItemByIdResponse401
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
) -> Response[GetItemByIdResponse401]:
    """Retrieve a single order item

     This endpoint will retrieve a single order item specified in the request.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetItemByIdResponse401]
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
) -> Optional[GetItemByIdResponse401]:
    """Retrieve a single order item

     This endpoint will retrieve a single order item specified in the request.

    Args:
        order_id (Union[int, str]):
        order_item_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetItemByIdResponse401
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            order_item_id=order_item_id,
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
