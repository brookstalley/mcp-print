from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_products_response_401 import GetProductsResponse401
from ...models.get_products_selling_region_name import GetProductsSellingRegionName
from ...models.get_products_sort_direction import GetProductsSortDirection
from ...models.get_products_sort_type import GetProductsSortType
from ...models.technique_enum import TechniqueEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    category_ids: Union[Unset, list[int]] = UNSET,
    colors: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
    new: Union[Unset, bool] = False,
    offset: Union[Unset, int] = 0,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[Unset, GetProductsSellingRegionName] = GetProductsSellingRegionName.WORLDWIDE,
    sort_direction: Union[Unset, GetProductsSortDirection] = GetProductsSortDirection.DESCENDING,
    sort_type: Union[Unset, GetProductsSortType] = UNSET,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    destination_country: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    params: dict[str, Any] = {}

    json_category_ids: Union[Unset, list[int]] = UNSET
    if not isinstance(category_ids, Unset):
        json_category_ids = category_ids

    params["category_ids"] = json_category_ids

    json_colors: Union[Unset, list[str]] = UNSET
    if not isinstance(colors, Unset):
        json_colors = colors

    params["colors"] = json_colors

    params["limit"] = limit

    params["new"] = new

    params["offset"] = offset

    json_placements: Union[Unset, list[str]] = UNSET
    if not isinstance(placements, Unset):
        json_placements = placements

    params["placements"] = json_placements

    json_selling_region_name: Union[Unset, str] = UNSET
    if not isinstance(selling_region_name, Unset):
        json_selling_region_name = selling_region_name.value

    params["selling_region_name"] = json_selling_region_name

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sort_direction"] = json_sort_direction

    json_sort_type: Union[Unset, str] = UNSET
    if not isinstance(sort_type, Unset):
        json_sort_type = sort_type.value

    params["sort_type"] = json_sort_type

    json_techniques: Union[Unset, list[str]] = UNSET
    if not isinstance(techniques, Unset):
        json_techniques = []
        for techniques_item_data in techniques:
            techniques_item = techniques_item_data.value
            json_techniques.append(techniques_item)

    params["techniques"] = json_techniques

    params["destination_country"] = destination_country

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/catalog-products",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetProductsResponse401]:
    if response.status_code == 401:
        response_401 = GetProductsResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetProductsResponse401]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category_ids: Union[Unset, list[int]] = UNSET,
    colors: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
    new: Union[Unset, bool] = False,
    offset: Union[Unset, int] = 0,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[Unset, GetProductsSellingRegionName] = GetProductsSellingRegionName.WORLDWIDE,
    sort_direction: Union[Unset, GetProductsSortDirection] = GetProductsSortDirection.DESCENDING,
    sort_type: Union[Unset, GetProductsSortType] = UNSET,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    destination_country: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[GetProductsResponse401]:
    r"""Retrieve a list of catalog products

     This endpoint retrieves a list of the products available in Printful's catalog. The list is
    paginated and can be filtered using various filters. The information returned includes details on
    how each product can be designed, such as the available placements, techniques, and additional
    options.
    For a visual representation of the design data, please see the following diagram:
    [<img src=\"images/catalog/design_data_diagram.png?center\" width=\"700\" alt=\"Design data
    diagram\"/>](images/catalog/design_data_diagram.png)

    Args:
        category_ids (Union[Unset, list[int]]):
        colors (Union[Unset, list[str]]):
        limit (Union[Unset, int]):  Default: 20.
        new (Union[Unset, bool]):  Default: False.
        offset (Union[Unset, int]):  Default: 0.
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, GetProductsSellingRegionName]):  Default:
            GetProductsSellingRegionName.WORLDWIDE.
        sort_direction (Union[Unset, GetProductsSortDirection]):  Default:
            GetProductsSortDirection.DESCENDING.
        sort_type (Union[Unset, GetProductsSortType]):
        techniques (Union[Unset, list[TechniqueEnum]]):
        destination_country (Union[Unset, str]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsResponse401]
    """

    kwargs = _get_kwargs(
        category_ids=category_ids,
        colors=colors,
        limit=limit,
        new=new,
        offset=offset,
        placements=placements,
        selling_region_name=selling_region_name,
        sort_direction=sort_direction,
        sort_type=sort_type,
        techniques=techniques,
        destination_country=destination_country,
        x_pf_language=x_pf_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category_ids: Union[Unset, list[int]] = UNSET,
    colors: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
    new: Union[Unset, bool] = False,
    offset: Union[Unset, int] = 0,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[Unset, GetProductsSellingRegionName] = GetProductsSellingRegionName.WORLDWIDE,
    sort_direction: Union[Unset, GetProductsSortDirection] = GetProductsSortDirection.DESCENDING,
    sort_type: Union[Unset, GetProductsSortType] = UNSET,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    destination_country: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[GetProductsResponse401]:
    r"""Retrieve a list of catalog products

     This endpoint retrieves a list of the products available in Printful's catalog. The list is
    paginated and can be filtered using various filters. The information returned includes details on
    how each product can be designed, such as the available placements, techniques, and additional
    options.
    For a visual representation of the design data, please see the following diagram:
    [<img src=\"images/catalog/design_data_diagram.png?center\" width=\"700\" alt=\"Design data
    diagram\"/>](images/catalog/design_data_diagram.png)

    Args:
        category_ids (Union[Unset, list[int]]):
        colors (Union[Unset, list[str]]):
        limit (Union[Unset, int]):  Default: 20.
        new (Union[Unset, bool]):  Default: False.
        offset (Union[Unset, int]):  Default: 0.
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, GetProductsSellingRegionName]):  Default:
            GetProductsSellingRegionName.WORLDWIDE.
        sort_direction (Union[Unset, GetProductsSortDirection]):  Default:
            GetProductsSortDirection.DESCENDING.
        sort_type (Union[Unset, GetProductsSortType]):
        techniques (Union[Unset, list[TechniqueEnum]]):
        destination_country (Union[Unset, str]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsResponse401
    """

    return sync_detailed(
        client=client,
        category_ids=category_ids,
        colors=colors,
        limit=limit,
        new=new,
        offset=offset,
        placements=placements,
        selling_region_name=selling_region_name,
        sort_direction=sort_direction,
        sort_type=sort_type,
        techniques=techniques,
        destination_country=destination_country,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category_ids: Union[Unset, list[int]] = UNSET,
    colors: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
    new: Union[Unset, bool] = False,
    offset: Union[Unset, int] = 0,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[Unset, GetProductsSellingRegionName] = GetProductsSellingRegionName.WORLDWIDE,
    sort_direction: Union[Unset, GetProductsSortDirection] = GetProductsSortDirection.DESCENDING,
    sort_type: Union[Unset, GetProductsSortType] = UNSET,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    destination_country: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[GetProductsResponse401]:
    r"""Retrieve a list of catalog products

     This endpoint retrieves a list of the products available in Printful's catalog. The list is
    paginated and can be filtered using various filters. The information returned includes details on
    how each product can be designed, such as the available placements, techniques, and additional
    options.
    For a visual representation of the design data, please see the following diagram:
    [<img src=\"images/catalog/design_data_diagram.png?center\" width=\"700\" alt=\"Design data
    diagram\"/>](images/catalog/design_data_diagram.png)

    Args:
        category_ids (Union[Unset, list[int]]):
        colors (Union[Unset, list[str]]):
        limit (Union[Unset, int]):  Default: 20.
        new (Union[Unset, bool]):  Default: False.
        offset (Union[Unset, int]):  Default: 0.
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, GetProductsSellingRegionName]):  Default:
            GetProductsSellingRegionName.WORLDWIDE.
        sort_direction (Union[Unset, GetProductsSortDirection]):  Default:
            GetProductsSortDirection.DESCENDING.
        sort_type (Union[Unset, GetProductsSortType]):
        techniques (Union[Unset, list[TechniqueEnum]]):
        destination_country (Union[Unset, str]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductsResponse401]
    """

    kwargs = _get_kwargs(
        category_ids=category_ids,
        colors=colors,
        limit=limit,
        new=new,
        offset=offset,
        placements=placements,
        selling_region_name=selling_region_name,
        sort_direction=sort_direction,
        sort_type=sort_type,
        techniques=techniques,
        destination_country=destination_country,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category_ids: Union[Unset, list[int]] = UNSET,
    colors: Union[Unset, list[str]] = UNSET,
    limit: Union[Unset, int] = 20,
    new: Union[Unset, bool] = False,
    offset: Union[Unset, int] = 0,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[Unset, GetProductsSellingRegionName] = GetProductsSellingRegionName.WORLDWIDE,
    sort_direction: Union[Unset, GetProductsSortDirection] = GetProductsSortDirection.DESCENDING,
    sort_type: Union[Unset, GetProductsSortType] = UNSET,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    destination_country: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[GetProductsResponse401]:
    r"""Retrieve a list of catalog products

     This endpoint retrieves a list of the products available in Printful's catalog. The list is
    paginated and can be filtered using various filters. The information returned includes details on
    how each product can be designed, such as the available placements, techniques, and additional
    options.
    For a visual representation of the design data, please see the following diagram:
    [<img src=\"images/catalog/design_data_diagram.png?center\" width=\"700\" alt=\"Design data
    diagram\"/>](images/catalog/design_data_diagram.png)

    Args:
        category_ids (Union[Unset, list[int]]):
        colors (Union[Unset, list[str]]):
        limit (Union[Unset, int]):  Default: 20.
        new (Union[Unset, bool]):  Default: False.
        offset (Union[Unset, int]):  Default: 0.
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, GetProductsSellingRegionName]):  Default:
            GetProductsSellingRegionName.WORLDWIDE.
        sort_direction (Union[Unset, GetProductsSortDirection]):  Default:
            GetProductsSortDirection.DESCENDING.
        sort_type (Union[Unset, GetProductsSortType]):
        techniques (Union[Unset, list[TechniqueEnum]]):
        destination_country (Union[Unset, str]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductsResponse401
    """

    return (
        await asyncio_detailed(
            client=client,
            category_ids=category_ids,
            colors=colors,
            limit=limit,
            new=new,
            offset=offset,
            placements=placements,
            selling_region_name=selling_region_name,
            sort_direction=sort_direction,
            sort_type=sort_type,
            techniques=techniques,
            destination_country=destination_country,
            x_pf_language=x_pf_language,
        )
    ).parsed
