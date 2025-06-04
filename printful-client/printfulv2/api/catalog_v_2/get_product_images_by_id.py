from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_images_by_id_response_200 import GetProductImagesByIdResponse200
from ...models.get_product_images_by_id_response_401 import GetProductImagesByIdResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    mockup_style_ids: Union[Unset, int] = UNSET,
    colors: Union[Unset, str] = UNSET,
    placement: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    params: dict[str, Any] = {}

    params["mockup_style_ids"] = mockup_style_ids

    params["colors"] = colors

    params["placement"] = placement

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-products/{id}/images",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]:
    if response.status_code == 200:
        response_200 = GetProductImagesByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetProductImagesByIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]:
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
    mockup_style_ids: Union[Unset, int] = UNSET,
    colors: Union[Unset, str] = UNSET,
    placement: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]:
    """Retrieve blank images for a catalog product

     This feature helps to fetch blank images for a catalog product. These blank images are always white
    and semi-transparent and can be colored by the user on the client-side as per the specified color in
    the `data.images.background_color` field. For some mockups the `data.images.background_image` could
    apply. The endpoint allows filtering of the result based on the type of the mockup, the placement,
    and the color of the product.

    Args:
        id (int):
        mockup_style_ids (Union[Unset, int]):  Example: 1, 2, 3.
        colors (Union[Unset, str]):  Example: black,red.
        placement (Union[Unset, str]):  Example: front.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
        mockup_style_ids=mockup_style_ids,
        colors=colors,
        placement=placement,
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
    mockup_style_ids: Union[Unset, int] = UNSET,
    colors: Union[Unset, str] = UNSET,
    placement: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]:
    """Retrieve blank images for a catalog product

     This feature helps to fetch blank images for a catalog product. These blank images are always white
    and semi-transparent and can be colored by the user on the client-side as per the specified color in
    the `data.images.background_color` field. For some mockups the `data.images.background_image` could
    apply. The endpoint allows filtering of the result based on the type of the mockup, the placement,
    and the color of the product.

    Args:
        id (int):
        mockup_style_ids (Union[Unset, int]):  Example: 1, 2, 3.
        colors (Union[Unset, str]):  Example: black,red.
        placement (Union[Unset, str]):  Example: front.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]
    """

    return sync_detailed(
        id=id,
        client=client,
        mockup_style_ids=mockup_style_ids,
        colors=colors,
        placement=placement,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    mockup_style_ids: Union[Unset, int] = UNSET,
    colors: Union[Unset, str] = UNSET,
    placement: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]:
    """Retrieve blank images for a catalog product

     This feature helps to fetch blank images for a catalog product. These blank images are always white
    and semi-transparent and can be colored by the user on the client-side as per the specified color in
    the `data.images.background_color` field. For some mockups the `data.images.background_image` could
    apply. The endpoint allows filtering of the result based on the type of the mockup, the placement,
    and the color of the product.

    Args:
        id (int):
        mockup_style_ids (Union[Unset, int]):  Example: 1, 2, 3.
        colors (Union[Unset, str]):  Example: black,red.
        placement (Union[Unset, str]):  Example: front.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
        mockup_style_ids=mockup_style_ids,
        colors=colors,
        placement=placement,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    mockup_style_ids: Union[Unset, int] = UNSET,
    colors: Union[Unset, str] = UNSET,
    placement: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]]:
    """Retrieve blank images for a catalog product

     This feature helps to fetch blank images for a catalog product. These blank images are always white
    and semi-transparent and can be colored by the user on the client-side as per the specified color in
    the `data.images.background_color` field. For some mockups the `data.images.background_image` could
    apply. The endpoint allows filtering of the result based on the type of the mockup, the placement,
    and the color of the product.

    Args:
        id (int):
        mockup_style_ids (Union[Unset, int]):  Example: 1, 2, 3.
        colors (Union[Unset, str]):  Example: black,red.
        placement (Union[Unset, str]):  Example: front.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProductImagesByIdResponse200, GetProductImagesByIdResponse401]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            mockup_style_ids=mockup_style_ids,
            colors=colors,
            placement=placement,
            x_pf_language=x_pf_language,
        )
    ).parsed
