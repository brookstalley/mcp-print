from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_invoice_by_order_id_response_200 import GetInvoiceByOrderIdResponse200
from ...models.get_invoice_by_order_id_response_401 import GetInvoiceByOrderIdResponse401
from ...types import UNSET, Response, Unset


def _get_kwargs(
    order_id: Union[int, str],
    *,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/orders/{order_id}/invoices",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]:
    if response.status_code == 200:
        response_200 = GetInvoiceByOrderIdResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetInvoiceByOrderIdResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]:
    """Retrieve an invoice

     Returns the invoice for an order as a base64 encoded document. Decoding the base64 content can be
    different depending on the client, for most browsers this format will alow you to view and display
    the invoice `data:application/pdf;base64,{the_base_64_content_string}`.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]:
    """Retrieve an invoice

     Returns the invoice for an order as a base64 encoded document. Decoding the base64 content can be
    different depending on the client, for most browsers this format will alow you to view and display
    the invoice `data:application/pdf;base64,{the_base_64_content_string}`.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]
    """

    return sync_detailed(
        order_id=order_id,
        client=client,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]:
    """Retrieve an invoice

     Returns the invoice for an order as a base64 encoded document. Decoding the base64 content can be
    different depending on the client, for most browsers this format will alow you to view and display
    the invoice `data:application/pdf;base64,{the_base_64_content_string}`.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]
    """

    kwargs = _get_kwargs(
        order_id=order_id,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    order_id: Union[int, str],
    *,
    client: AuthenticatedClient,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]]:
    """Retrieve an invoice

     Returns the invoice for an order as a base64 encoded document. Decoding the base64 content can be
    different depending on the client, for most browsers this format will alow you to view and display
    the invoice `data:application/pdf;base64,{the_base_64_content_string}`.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetInvoiceByOrderIdResponse200, GetInvoiceByOrderIdResponse401]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
