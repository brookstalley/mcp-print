from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_product_shipping_countries_by_id_response_200 import GetProductShippingCountriesByIdResponse200
from ...models.get_product_shipping_countries_by_id_response_401 import GetProductShippingCountriesByIdResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    x_pf_language: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_language, Unset):
        headers["X-PF-Language"] = x_pf_language

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/catalog-products/{id}/shipping-countries",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]:
    if response.status_code == 200:
        response_200 = GetProductShippingCountriesByIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetProductShippingCountriesByIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]:
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
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]:
    """Retrieve the shipping countries for a Product

     Retrieve the list of countries the Catalog Product can be shipped to.

    Args:
        id (int):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
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
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]:
    """Retrieve the shipping countries for a Product

     Retrieve the list of countries the Catalog Product can be shipped to.

    Args:
        id (int):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]
    """

    return sync_detailed(
        id=id,
        client=client,
        x_pf_language=x_pf_language,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Response[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]:
    """Retrieve the shipping countries for a Product

     Retrieve the list of countries the Catalog Product can be shipped to.

    Args:
        id (int):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]
    """

    kwargs = _get_kwargs(
        id=id,
        x_pf_language=x_pf_language,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    x_pf_language: Union[Unset, str] = UNSET,
) -> Optional[Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]]:
    """Retrieve the shipping countries for a Product

     Retrieve the list of countries the Catalog Product can be shipped to.

    Args:
        id (int):
        x_pf_language (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProductShippingCountriesByIdResponse200, GetProductShippingCountriesByIdResponse401]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            x_pf_language=x_pf_language,
        )
    ).parsed
