from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_categories_response_200 import GetCategoriesResponse200
from ...models.get_categories_response_401 import GetCategoriesResponse401
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/catalog-categories",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetCategoriesResponse200, GetCategoriesResponse401]]:
    if response.status_code == 200:
        response_200 = GetCategoriesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetCategoriesResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetCategoriesResponse200, GetCategoriesResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetCategoriesResponse200, GetCategoriesResponse401]]:
    r"""Retrieve a list of catalog categories

     Returns list of all categories that are present in the catalog. The categories specify the type of
    the product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that
    the product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCategoriesResponse200, GetCategoriesResponse401]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetCategoriesResponse200, GetCategoriesResponse401]]:
    r"""Retrieve a list of catalog categories

     Returns list of all categories that are present in the catalog. The categories specify the type of
    the product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that
    the product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCategoriesResponse200, GetCategoriesResponse401]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetCategoriesResponse200, GetCategoriesResponse401]]:
    r"""Retrieve a list of catalog categories

     Returns list of all categories that are present in the catalog. The categories specify the type of
    the product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that
    the product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCategoriesResponse200, GetCategoriesResponse401]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetCategoriesResponse200, GetCategoriesResponse401]]:
    r"""Retrieve a list of catalog categories

     Returns list of all categories that are present in the catalog. The categories specify the type of
    the product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that
    the product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCategoriesResponse200, GetCategoriesResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
