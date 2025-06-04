from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_variant_stock_availability_by_id_response_400 import GetVariantStockAvailabilityByIdResponse400
from ...models.get_variant_stock_availability_by_id_response_401 import GetVariantStockAvailabilityByIdResponse401
from ...models.get_variant_stock_availability_by_id_response_403 import GetVariantStockAvailabilityByIdResponse403
from ...models.get_variant_stock_availability_by_id_response_404 import GetVariantStockAvailabilityByIdResponse404
from ...models.get_variant_stock_availability_by_id_selling_region_name import (
    GetVariantStockAvailabilityByIdSellingRegionName,
)
from ...models.technique_enum import TechniqueEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    selling_region_name: Union[
        Unset, GetVariantStockAvailabilityByIdSellingRegionName
    ] = GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    params: dict[str, Any] = {}

    json_techniques: Union[Unset, list[str]] = UNSET
    if not isinstance(techniques, Unset):
        json_techniques = []
        for techniques_item_data in techniques:
            techniques_item = techniques_item_data.value
            json_techniques.append(techniques_item)

    params["techniques"] = json_techniques

    json_selling_region_name: Union[Unset, str] = UNSET
    if not isinstance(selling_region_name, Unset):
        json_selling_region_name = selling_region_name.value

    params["selling_region_name"] = json_selling_region_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-variants/{id}/availability",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetVariantStockAvailabilityByIdResponse400,
        GetVariantStockAvailabilityByIdResponse401,
        GetVariantStockAvailabilityByIdResponse403,
        GetVariantStockAvailabilityByIdResponse404,
    ]
]:
    if response.status_code == 400:
        response_400 = GetVariantStockAvailabilityByIdResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetVariantStockAvailabilityByIdResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GetVariantStockAvailabilityByIdResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = GetVariantStockAvailabilityByIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetVariantStockAvailabilityByIdResponse400,
        GetVariantStockAvailabilityByIdResponse401,
        GetVariantStockAvailabilityByIdResponse403,
        GetVariantStockAvailabilityByIdResponse404,
    ]
]:
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
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    selling_region_name: Union[
        Unset, GetVariantStockAvailabilityByIdSellingRegionName
    ] = GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        GetVariantStockAvailabilityByIdResponse400,
        GetVariantStockAvailabilityByIdResponse401,
        GetVariantStockAvailabilityByIdResponse403,
        GetVariantStockAvailabilityByIdResponse404,
    ]
]:
    """Retrieve catalog variant stock availability

     Provides information about the catalog variant stock status. Stock availability is grouped by
    variants &rarr; techniques &rarr; selling regions.

    Args:
        id (int):
        techniques (Union[Unset, list[TechniqueEnum]]):
        selling_region_name (Union[Unset, GetVariantStockAvailabilityByIdSellingRegionName]):
            Default: GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetVariantStockAvailabilityByIdResponse400, GetVariantStockAvailabilityByIdResponse401, GetVariantStockAvailabilityByIdResponse403, GetVariantStockAvailabilityByIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        techniques=techniques,
        selling_region_name=selling_region_name,
        x_pf_language=x_pf_language,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    selling_region_name: Union[
        Unset, GetVariantStockAvailabilityByIdSellingRegionName
    ] = GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        GetVariantStockAvailabilityByIdResponse400,
        GetVariantStockAvailabilityByIdResponse401,
        GetVariantStockAvailabilityByIdResponse403,
        GetVariantStockAvailabilityByIdResponse404,
    ]
]:
    """Retrieve catalog variant stock availability

     Provides information about the catalog variant stock status. Stock availability is grouped by
    variants &rarr; techniques &rarr; selling regions.

    Args:
        id (int):
        techniques (Union[Unset, list[TechniqueEnum]]):
        selling_region_name (Union[Unset, GetVariantStockAvailabilityByIdSellingRegionName]):
            Default: GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetVariantStockAvailabilityByIdResponse400, GetVariantStockAvailabilityByIdResponse401, GetVariantStockAvailabilityByIdResponse403, GetVariantStockAvailabilityByIdResponse404]
    """

    return sync_detailed(
        id=id,
        client=client,
        techniques=techniques,
        selling_region_name=selling_region_name,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    selling_region_name: Union[
        Unset, GetVariantStockAvailabilityByIdSellingRegionName
    ] = GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        GetVariantStockAvailabilityByIdResponse400,
        GetVariantStockAvailabilityByIdResponse401,
        GetVariantStockAvailabilityByIdResponse403,
        GetVariantStockAvailabilityByIdResponse404,
    ]
]:
    """Retrieve catalog variant stock availability

     Provides information about the catalog variant stock status. Stock availability is grouped by
    variants &rarr; techniques &rarr; selling regions.

    Args:
        id (int):
        techniques (Union[Unset, list[TechniqueEnum]]):
        selling_region_name (Union[Unset, GetVariantStockAvailabilityByIdSellingRegionName]):
            Default: GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetVariantStockAvailabilityByIdResponse400, GetVariantStockAvailabilityByIdResponse401, GetVariantStockAvailabilityByIdResponse403, GetVariantStockAvailabilityByIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        techniques=techniques,
        selling_region_name=selling_region_name,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    techniques: Union[Unset, list[TechniqueEnum]] = UNSET,
    selling_region_name: Union[
        Unset, GetVariantStockAvailabilityByIdSellingRegionName
    ] = GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        GetVariantStockAvailabilityByIdResponse400,
        GetVariantStockAvailabilityByIdResponse401,
        GetVariantStockAvailabilityByIdResponse403,
        GetVariantStockAvailabilityByIdResponse404,
    ]
]:
    """Retrieve catalog variant stock availability

     Provides information about the catalog variant stock status. Stock availability is grouped by
    variants &rarr; techniques &rarr; selling regions.

    Args:
        id (int):
        techniques (Union[Unset, list[TechniqueEnum]]):
        selling_region_name (Union[Unset, GetVariantStockAvailabilityByIdSellingRegionName]):
            Default: GetVariantStockAvailabilityByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetVariantStockAvailabilityByIdResponse400, GetVariantStockAvailabilityByIdResponse401, GetVariantStockAvailabilityByIdResponse403, GetVariantStockAvailabilityByIdResponse404]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            techniques=techniques,
            selling_region_name=selling_region_name,
            x_pf_language=x_pf_language,
        )
    ).parsed
