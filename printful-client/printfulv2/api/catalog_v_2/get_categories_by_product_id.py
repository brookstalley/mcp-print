from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_categories_by_product_id_response_200 import GetCategoriesByProductIdResponse200
from ...models.get_categories_by_product_id_response_401 import GetCategoriesByProductIdResponse401
from ...models.get_categories_by_product_id_selling_region_name import GetCategoriesByProductIdSellingRegionName
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    selling_region_name: Union[
        Unset, GetCategoriesByProductIdSellingRegionName
    ] = GetCategoriesByProductIdSellingRegionName.WORLDWIDE,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_selling_region_name: Union[Unset, str] = UNSET
    if not isinstance(selling_region_name, Unset):
        json_selling_region_name = selling_region_name.value

    params["selling_region_name"] = json_selling_region_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-products/{id}/catalog-categories",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]:
    if response.status_code == 200:
        response_200 = GetCategoriesByProductIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetCategoriesByProductIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]:
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
    selling_region_name: Union[
        Unset, GetCategoriesByProductIdSellingRegionName
    ] = GetCategoriesByProductIdSellingRegionName.WORLDWIDE,
) -> Response[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]:
    r"""Retrieve a list of catalog product categories

     To retrieve information about a particular products categories, use this feature. It returns details
    about the catalog categories associated with the catalog product. Categories help identify the type
    of product associated with them. For instance, the category \"Men's T-shirts\" denotes that the
    product is a subgroup of T-shirts intended for men.

    Args:
        id (int):
        selling_region_name (Union[Unset, GetCategoriesByProductIdSellingRegionName]):  Default:
            GetCategoriesByProductIdSellingRegionName.WORLDWIDE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
        selling_region_name=selling_region_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    selling_region_name: Union[
        Unset, GetCategoriesByProductIdSellingRegionName
    ] = GetCategoriesByProductIdSellingRegionName.WORLDWIDE,
) -> Optional[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]:
    r"""Retrieve a list of catalog product categories

     To retrieve information about a particular products categories, use this feature. It returns details
    about the catalog categories associated with the catalog product. Categories help identify the type
    of product associated with them. For instance, the category \"Men's T-shirts\" denotes that the
    product is a subgroup of T-shirts intended for men.

    Args:
        id (int):
        selling_region_name (Union[Unset, GetCategoriesByProductIdSellingRegionName]):  Default:
            GetCategoriesByProductIdSellingRegionName.WORLDWIDE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]
    """

    return sync_detailed(
        id=id,
        client=client,
        selling_region_name=selling_region_name,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    selling_region_name: Union[
        Unset, GetCategoriesByProductIdSellingRegionName
    ] = GetCategoriesByProductIdSellingRegionName.WORLDWIDE,
) -> Response[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]:
    r"""Retrieve a list of catalog product categories

     To retrieve information about a particular products categories, use this feature. It returns details
    about the catalog categories associated with the catalog product. Categories help identify the type
    of product associated with them. For instance, the category \"Men's T-shirts\" denotes that the
    product is a subgroup of T-shirts intended for men.

    Args:
        id (int):
        selling_region_name (Union[Unset, GetCategoriesByProductIdSellingRegionName]):  Default:
            GetCategoriesByProductIdSellingRegionName.WORLDWIDE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
        selling_region_name=selling_region_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    selling_region_name: Union[
        Unset, GetCategoriesByProductIdSellingRegionName
    ] = GetCategoriesByProductIdSellingRegionName.WORLDWIDE,
) -> Optional[Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]]:
    r"""Retrieve a list of catalog product categories

     To retrieve information about a particular products categories, use this feature. It returns details
    about the catalog categories associated with the catalog product. Categories help identify the type
    of product associated with them. For instance, the category \"Men's T-shirts\" denotes that the
    product is a subgroup of T-shirts intended for men.

    Args:
        id (int):
        selling_region_name (Union[Unset, GetCategoriesByProductIdSellingRegionName]):  Default:
            GetCategoriesByProductIdSellingRegionName.WORLDWIDE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetCategoriesByProductIdResponse200, GetCategoriesByProductIdResponse401]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            selling_region_name=selling_region_name,
        )
    ).parsed
