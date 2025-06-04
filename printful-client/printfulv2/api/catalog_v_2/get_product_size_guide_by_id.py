from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_size_guide_by_id_response_200 import GetProductSizeGuideByIdResponse200
from ...models.get_product_size_guide_by_id_response_404 import GetProductSizeGuideByIdResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    unit: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    params: dict[str, Any] = {}

    params["unit"] = unit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-products/{id}/sizes",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]:
    if response.status_code == 200:
        response_200 = GetProductSizeGuideByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GetProductSizeGuideByIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]:
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
    unit: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]:
    """Retrieve size guide for a catalog product

     Returns information about the size guide for a specific product.

    Args:
        id (int):
        unit (Union[Unset, str]):  Example: inches,cm.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        unit=unit,
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
    unit: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]:
    """Retrieve size guide for a catalog product

     Returns information about the size guide for a specific product.

    Args:
        id (int):
        unit (Union[Unset, str]):  Example: inches,cm.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]
    """

    return sync_detailed(
        id=id,
        client=client,
        unit=unit,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    unit: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]:
    """Retrieve size guide for a catalog product

     Returns information about the size guide for a specific product.

    Args:
        id (int):
        unit (Union[Unset, str]):  Example: inches,cm.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        unit=unit,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    unit: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]]:
    """Retrieve size guide for a catalog product

     Returns information about the size guide for a specific product.

    Args:
        id (int):
        unit (Union[Unset, str]):  Example: inches,cm.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProductSizeGuideByIdResponse200, GetProductSizeGuideByIdResponse404]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            unit=unit,
            x_pf_language=x_pf_language,
        )
    ).parsed
