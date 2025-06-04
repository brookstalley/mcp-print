from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.retrieve_mockup_styles_by_product_id_response_401 import RetrieveMockupStylesByProductIdResponse401
from ...models.retrieve_mockup_styles_by_product_id_response_404 import RetrieveMockupStylesByProductIdResponse404
from ...models.retrieve_mockup_styles_by_product_id_selling_region_name import (
    RetrieveMockupStylesByProductIdSellingRegionName,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[
        Unset, RetrieveMockupStylesByProductIdSellingRegionName
    ] = RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    params: dict[str, Any] = {}

    json_placements: Union[Unset, list[str]] = UNSET
    if not isinstance(placements, Unset):
        json_placements = placements

    params["placements"] = json_placements

    json_selling_region_name: Union[Unset, str] = UNSET
    if not isinstance(selling_region_name, Unset):
        json_selling_region_name = selling_region_name.value

    params["selling_region_name"] = json_selling_region_name

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-products/{id}/mockup-styles",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]:
    if response.status_code == 401:
        response_401 = RetrieveMockupStylesByProductIdResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = RetrieveMockupStylesByProductIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]:
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
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[
        Unset, RetrieveMockupStylesByProductIdSellingRegionName
    ] = RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]:
    """Retrieve catalog product mockup styles

     Returns information about available mockup styles for specified catalog product.

    Args:
        id (int):
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, RetrieveMockupStylesByProductIdSellingRegionName]):
            Default: RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        placements=placements,
        selling_region_name=selling_region_name,
        offset=offset,
        limit=limit,
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
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[
        Unset, RetrieveMockupStylesByProductIdSellingRegionName
    ] = RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]:
    """Retrieve catalog product mockup styles

     Returns information about available mockup styles for specified catalog product.

    Args:
        id (int):
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, RetrieveMockupStylesByProductIdSellingRegionName]):
            Default: RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]
    """

    return sync_detailed(
        id=id,
        client=client,
        placements=placements,
        selling_region_name=selling_region_name,
        offset=offset,
        limit=limit,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[
        Unset, RetrieveMockupStylesByProductIdSellingRegionName
    ] = RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]:
    """Retrieve catalog product mockup styles

     Returns information about available mockup styles for specified catalog product.

    Args:
        id (int):
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, RetrieveMockupStylesByProductIdSellingRegionName]):
            Default: RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        placements=placements,
        selling_region_name=selling_region_name,
        offset=offset,
        limit=limit,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    placements: Union[Unset, list[str]] = UNSET,
    selling_region_name: Union[
        Unset, RetrieveMockupStylesByProductIdSellingRegionName
    ] = RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE,
    offset: Union[Unset, int] = UNSET,
    limit: Union[Unset, int] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]]:
    """Retrieve catalog product mockup styles

     Returns information about available mockup styles for specified catalog product.

    Args:
        id (int):
        placements (Union[Unset, list[str]]):
        selling_region_name (Union[Unset, RetrieveMockupStylesByProductIdSellingRegionName]):
            Default: RetrieveMockupStylesByProductIdSellingRegionName.WORLDWIDE.
        offset (Union[Unset, int]):
        limit (Union[Unset, int]):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RetrieveMockupStylesByProductIdResponse401, RetrieveMockupStylesByProductIdResponse404]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            placements=placements,
            selling_region_name=selling_region_name,
            offset=offset,
            limit=limit,
            x_pf_language=x_pf_language,
        )
    ).parsed
