from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_order_response_401 import DeleteOrderResponse401
from ...models.delete_order_response_404 import DeleteOrderResponse404
from ...models.delete_order_response_409 import DeleteOrderResponse409
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
        "method": "delete",
        "url": f"/v2/orders/{order_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 401:
        response_401 = DeleteOrderResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = DeleteOrderResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = DeleteOrderResponse409.from_dict(response.json())

        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]:
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
) -> Response[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]:
    r"""Delete an order

     <div class=\"alert alert-danger\">
      <strong>Warning:</strong> The DELETE HTTP method in version 2 of order in the
      API will delete the order if the order can be deleted. This is distinct from
      version 1 where the DELETE method will actually cancel the order rather than
      delete it. Please, keep this in mind if you are migrating to version 2 from
      version 1
    </div>

    Delete the order if it can be deleted. An order can be deleted if it's status is
    `draft`, `failed` or `cancelled`. The order must also have not been charged yet
    and there must be no payments pending.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]
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
) -> Optional[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]:
    r"""Delete an order

     <div class=\"alert alert-danger\">
      <strong>Warning:</strong> The DELETE HTTP method in version 2 of order in the
      API will delete the order if the order can be deleted. This is distinct from
      version 1 where the DELETE method will actually cancel the order rather than
      delete it. Please, keep this in mind if you are migrating to version 2 from
      version 1
    </div>

    Delete the order if it can be deleted. An order can be deleted if it's status is
    `draft`, `failed` or `cancelled`. The order must also have not been charged yet
    and there must be no payments pending.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]
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
) -> Response[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]:
    r"""Delete an order

     <div class=\"alert alert-danger\">
      <strong>Warning:</strong> The DELETE HTTP method in version 2 of order in the
      API will delete the order if the order can be deleted. This is distinct from
      version 1 where the DELETE method will actually cancel the order rather than
      delete it. Please, keep this in mind if you are migrating to version 2 from
      version 1
    </div>

    Delete the order if it can be deleted. An order can be deleted if it's status is
    `draft`, `failed` or `cancelled`. The order must also have not been charged yet
    and there must be no payments pending.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]
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
) -> Optional[Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]]:
    r"""Delete an order

     <div class=\"alert alert-danger\">
      <strong>Warning:</strong> The DELETE HTTP method in version 2 of order in the
      API will delete the order if the order can be deleted. This is distinct from
      version 1 where the DELETE method will actually cancel the order rather than
      delete it. Please, keep this in mind if you are migrating to version 2 from
      version 1
    </div>

    Delete the order if it can be deleted. An order can be deleted if it's status is
    `draft`, `failed` or `cancelled`. The order must also have not been charged yet
    and there must be no payments pending.

    Args:
        order_id (Union[int, str]):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeleteOrderResponse401, DeleteOrderResponse404, DeleteOrderResponse409]
    """

    return (
        await asyncio_detailed(
            order_id=order_id,
            client=client,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
