from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_prices_by_id_response_404 import GetProductPricesByIdResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    selling_region_name: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    params: dict[str, Any] = {}

    params["selling_region_name"] = selling_region_name

    params["currency"] = currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-products/{id}/prices",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetProductPricesByIdResponse404]:
    if response.status_code == 404:
        response_404 = GetProductPricesByIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetProductPricesByIdResponse404]:
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
    selling_region_name: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[GetProductPricesByIdResponse404]:
    r"""Retrieve catalog product prices


    Calculates prices for specific catalog product based on selling region and specified currency.
    Calculations also include Store discounts. Selling region is used to specify product production
    currency, that is the price that the product is natively manufactured in. Different selling regions
    might affect the overall price amount. Currency parameter is used only to define the currency that
    the prices will be displayed in.

    For more information on product pricing please refer to the information provided at
    https://www.printful.com/pricing
    <div class=\"alert alert-info\" style=\"word-wrap: break-word; padding: 16px; border-radius: 0;
    cursor: default; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;\">
        <p>
            When developing against either API be sure to inform your customers that a placement will be
    included in the price of the product. If one placement is provided that placement will be included
    in the price, if multiple are provided the included placement will generally be the placement that
    comes earliest in the list of placements at `/v2/catalog-products/71` (though the discount will
    generally be up to the price of the first placement in that list). Certain placements come with
    additional service fees, such as large embroidery, this additional price will never be included even
    if the only placement is large embroidery.
        </p>
        <p>
            There is a minor difference in the handling of prices for placements between V1 and V2.
            In V1 the price of the first placement is always null, this is because there
            is always a placement included in the price of each product. In V2 the price of placements
            is always displayed even if it is included in the price of the product because any
            placement can be included.
        </p>
    </div>

    Args:
        id (int):
        selling_region_name (Union[Unset, str]):  Example: worldwide.
        currency (Union[Unset, str]):  Example: USD.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductPricesByIdResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        selling_region_name=selling_region_name,
        currency=currency,
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
    selling_region_name: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[GetProductPricesByIdResponse404]:
    r"""Retrieve catalog product prices


    Calculates prices for specific catalog product based on selling region and specified currency.
    Calculations also include Store discounts. Selling region is used to specify product production
    currency, that is the price that the product is natively manufactured in. Different selling regions
    might affect the overall price amount. Currency parameter is used only to define the currency that
    the prices will be displayed in.

    For more information on product pricing please refer to the information provided at
    https://www.printful.com/pricing
    <div class=\"alert alert-info\" style=\"word-wrap: break-word; padding: 16px; border-radius: 0;
    cursor: default; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;\">
        <p>
            When developing against either API be sure to inform your customers that a placement will be
    included in the price of the product. If one placement is provided that placement will be included
    in the price, if multiple are provided the included placement will generally be the placement that
    comes earliest in the list of placements at `/v2/catalog-products/71` (though the discount will
    generally be up to the price of the first placement in that list). Certain placements come with
    additional service fees, such as large embroidery, this additional price will never be included even
    if the only placement is large embroidery.
        </p>
        <p>
            There is a minor difference in the handling of prices for placements between V1 and V2.
            In V1 the price of the first placement is always null, this is because there
            is always a placement included in the price of each product. In V2 the price of placements
            is always displayed even if it is included in the price of the product because any
            placement can be included.
        </p>
    </div>

    Args:
        id (int):
        selling_region_name (Union[Unset, str]):  Example: worldwide.
        currency (Union[Unset, str]):  Example: USD.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductPricesByIdResponse404
    """

    return sync_detailed(
        id=id,
        client=client,
        selling_region_name=selling_region_name,
        currency=currency,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    selling_region_name: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[GetProductPricesByIdResponse404]:
    r"""Retrieve catalog product prices


    Calculates prices for specific catalog product based on selling region and specified currency.
    Calculations also include Store discounts. Selling region is used to specify product production
    currency, that is the price that the product is natively manufactured in. Different selling regions
    might affect the overall price amount. Currency parameter is used only to define the currency that
    the prices will be displayed in.

    For more information on product pricing please refer to the information provided at
    https://www.printful.com/pricing
    <div class=\"alert alert-info\" style=\"word-wrap: break-word; padding: 16px; border-radius: 0;
    cursor: default; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;\">
        <p>
            When developing against either API be sure to inform your customers that a placement will be
    included in the price of the product. If one placement is provided that placement will be included
    in the price, if multiple are provided the included placement will generally be the placement that
    comes earliest in the list of placements at `/v2/catalog-products/71` (though the discount will
    generally be up to the price of the first placement in that list). Certain placements come with
    additional service fees, such as large embroidery, this additional price will never be included even
    if the only placement is large embroidery.
        </p>
        <p>
            There is a minor difference in the handling of prices for placements between V1 and V2.
            In V1 the price of the first placement is always null, this is because there
            is always a placement included in the price of each product. In V2 the price of placements
            is always displayed even if it is included in the price of the product because any
            placement can be included.
        </p>
    </div>

    Args:
        id (int):
        selling_region_name (Union[Unset, str]):  Example: worldwide.
        currency (Union[Unset, str]):  Example: USD.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetProductPricesByIdResponse404]
    """

    kwargs = _get_kwargs(
        id=id,
        selling_region_name=selling_region_name,
        currency=currency,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    selling_region_name: Union[Unset, str] = UNSET,
    currency: Union[Unset, str] = UNSET,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[GetProductPricesByIdResponse404]:
    r"""Retrieve catalog product prices


    Calculates prices for specific catalog product based on selling region and specified currency.
    Calculations also include Store discounts. Selling region is used to specify product production
    currency, that is the price that the product is natively manufactured in. Different selling regions
    might affect the overall price amount. Currency parameter is used only to define the currency that
    the prices will be displayed in.

    For more information on product pricing please refer to the information provided at
    https://www.printful.com/pricing
    <div class=\"alert alert-info\" style=\"word-wrap: break-word; padding: 16px; border-radius: 0;
    cursor: default; color: #31708f; background-color: #d9edf7; border-color: #bce8f1;\">
        <p>
            When developing against either API be sure to inform your customers that a placement will be
    included in the price of the product. If one placement is provided that placement will be included
    in the price, if multiple are provided the included placement will generally be the placement that
    comes earliest in the list of placements at `/v2/catalog-products/71` (though the discount will
    generally be up to the price of the first placement in that list). Certain placements come with
    additional service fees, such as large embroidery, this additional price will never be included even
    if the only placement is large embroidery.
        </p>
        <p>
            There is a minor difference in the handling of prices for placements between V1 and V2.
            In V1 the price of the first placement is always null, this is because there
            is always a placement included in the price of each product. In V2 the price of placements
            is always displayed even if it is included in the price of the product because any
            placement can be included.
        </p>
    </div>

    Args:
        id (int):
        selling_region_name (Union[Unset, str]):  Example: worldwide.
        currency (Union[Unset, str]):  Example: USD.
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetProductPricesByIdResponse404
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            selling_region_name=selling_region_name,
            currency=currency,
            x_pf_language=x_pf_language,
        )
    ).parsed
