from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_store_by_id_response_200 import GetStoreByIdResponse200
from ...models.get_store_by_id_response_401 import GetStoreByIdResponse401
from ...models.get_store_by_id_response_404 import GetStoreByIdResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    store_id: int,
    *,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/stores/{store_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]:
    if response.status_code == 200:
        response_200 = GetStoreByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetStoreByIdResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = GetStoreByIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    store_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]:
    """Retrieve a single store

     Get information about a single store.

    Args:
        store_id (int): ID of the resource, assigned by Printful Example: 1234.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    store_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]:
    """Retrieve a single store

     Get information about a single store.

    Args:
        store_id (int): ID of the resource, assigned by Printful Example: 1234.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]
    """

    return sync_detailed(
        store_id=store_id,
        client=client,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    store_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]:
    """Retrieve a single store

     Get information about a single store.

    Args:
        store_id (int): ID of the resource, assigned by Printful Example: 1234.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]
    """

    kwargs = _get_kwargs(
        store_id=store_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    store_id: int,
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]]:
    """Retrieve a single store

     Get information about a single store.

    Args:
        store_id (int): ID of the resource, assigned by Printful Example: 1234.
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStoreByIdResponse200, GetStoreByIdResponse401, GetStoreByIdResponse404]
    """

    return (
        await asyncio_detailed(
            store_id=store_id,
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
