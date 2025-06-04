from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_category_by_id_response_200 import GetCategoryByIdResponse200
from ...models.get_category_by_id_response_401 import GetCategoryByIdResponse401
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-categories/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]:
    if response.status_code == 200:
        response_200 = GetCategoryByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetCategoryByIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]:
    r"""Retrieve information about specific category

     Returns information about a specific catalog category. The categories specify the type of the
    product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that the
    product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]:
    r"""Retrieve information about specific category

     Returns information about a specific catalog category. The categories specify the type of the
    product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that the
    product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]:
    r"""Retrieve information about specific category

     Returns information about a specific catalog category. The categories specify the type of the
    product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that the
    product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]]:
    r"""Retrieve information about specific category

     Returns information about a specific catalog category. The categories specify the type of the
    product that is associated with it. For example, the category \"Men’s T-shirts\" indicates that the
    product is a subgroup of T-shirts specifically targeted at Men.
    Categories can be used to filter the product list by specific tags [See
    categories_ids](#operation/getProducts)

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCategoryByIdResponse200, GetCategoryByIdResponse401]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
