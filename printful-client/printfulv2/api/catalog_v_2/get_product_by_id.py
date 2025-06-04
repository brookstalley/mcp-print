from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_by_id_response_401 import GetProductByIdResponse401
from ...models.get_product_by_id_selling_region_name import GetProductByIdSellingRegionName
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    selling_region_name: Union[Unset, GetProductByIdSellingRegionName] = GetProductByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    params: dict[str, Any] = {}

    json_selling_region_name: Union[Unset, str] = UNSET
    if not isinstance(selling_region_name, Unset):
        json_selling_region_name = selling_region_name.value

    params["selling_region_name"] = json_selling_region_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-products/{id}",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetProductByIdResponse401]:
    if response.status_code == 401:
        response_401 = GetProductByIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetProductByIdResponse401]:
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
    selling_region_name: Union[Unset, GetProductByIdSellingRegionName] = GetProductByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[GetProductByIdResponse401]:
    """Retrieve a single catalog product

     Returns information about a single specified catalog product. [See catalog
    product](#tag/Catalog-v2/What-is-a-catalog-product)

    Args:
        id (int):
        selling_region_name (Union[Unset, GetProductByIdSellingRegionName]):  Default:
            GetProductByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductByIdResponse401]
    """

    kwargs = _get_kwargs(
        id=id,
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
    selling_region_name: Union[Unset, GetProductByIdSellingRegionName] = GetProductByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[GetProductByIdResponse401]:
    """Retrieve a single catalog product

     Returns information about a single specified catalog product. [See catalog
    product](#tag/Catalog-v2/What-is-a-catalog-product)

    Args:
        id (int):
        selling_region_name (Union[Unset, GetProductByIdSellingRegionName]):  Default:
            GetProductByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductByIdResponse401
    """

    return sync_detailed(
        id=id,
        client=client,
        selling_region_name=selling_region_name,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    selling_region_name: Union[Unset, GetProductByIdSellingRegionName] = GetProductByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[GetProductByIdResponse401]:
    """Retrieve a single catalog product

     Returns information about a single specified catalog product. [See catalog
    product](#tag/Catalog-v2/What-is-a-catalog-product)

    Args:
        id (int):
        selling_region_name (Union[Unset, GetProductByIdSellingRegionName]):  Default:
            GetProductByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductByIdResponse401]
    """

    kwargs = _get_kwargs(
        id=id,
        selling_region_name=selling_region_name,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    selling_region_name: Union[Unset, GetProductByIdSellingRegionName] = GetProductByIdSellingRegionName.WORLDWIDE,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[GetProductByIdResponse401]:
    """Retrieve a single catalog product

     Returns information about a single specified catalog product. [See catalog
    product](#tag/Catalog-v2/What-is-a-catalog-product)

    Args:
        id (int):
        selling_region_name (Union[Unset, GetProductByIdSellingRegionName]):  Default:
            GetProductByIdSellingRegionName.WORLDWIDE.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductByIdResponse401
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            selling_region_name=selling_region_name,
            x_pf_language=x_pf_language,
        )
    ).parsed
