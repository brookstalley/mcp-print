from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_stores_response_200 import GetStoresResponse200
from ...models.get_stores_response_401 import GetStoresResponse401
from ...models.get_stores_response_404 import GetStoresResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/stores",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]:
    if response.status_code == 200:
        response_200 = GetStoresResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetStoresResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = GetStoresResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]:
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
) -> Response[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]:
    """Retrieves a list of stores

     Retrieves a list of all stores available to the token. If the token is a store level token it will
    return only the one store, if it is an account level token it will return all stores available to
    the account.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]
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
) -> Optional[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]:
    """Retrieves a list of stores

     Retrieves a list of all stores available to the token. If the token is a store level token it will
    return only the one store, if it is an account level token it will return all stores available to
    the account.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]
    """

    return sync_detailed(
        client=client,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]:
    """Retrieves a list of stores

     Retrieves a list of all stores available to the token. If the token is a store level token it will
    return only the one store, if it is an account level token it will return all stores available to
    the account.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]
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
) -> Optional[Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]]:
    """Retrieves a list of stores

     Retrieves a list of all stores available to the token. If the token is a store level token it will
    return only the one store, if it is an account level token it will return all stores available to
    the account.

    Args:
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetStoresResponse200, GetStoresResponse401, GetStoresResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
