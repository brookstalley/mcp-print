from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_order_estimation_task_response_200 import GetOrderEstimationTaskResponse200
from ...models.get_order_estimation_task_response_401 import GetOrderEstimationTaskResponse401
from ...models.get_order_estimation_task_response_404 import GetOrderEstimationTaskResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    params: dict[str, Any] = {}

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/order-estimation-tasks",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
]:
    if response.status_code == 200:
        response_200 = GetOrderEstimationTaskResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetOrderEstimationTaskResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = GetOrderEstimationTaskResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
]:
    """Retrieve an order estimation task

     Retrieve an order cost estimation task from a specific store.
    Estimation results are only available for one hour after cost estimation task is done.

    Args:
        id (str):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
]:
    """Retrieve an order estimation task

     Retrieve an order cost estimation task from a specific store.
    Estimation results are only available for one hour after cost estimation task is done.

    Args:
        id (str):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
    """

    return sync_detailed(
        client=client,
        id=id,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
]:
    """Retrieve an order estimation task

     Retrieve an order cost estimation task from a specific store.
    Estimation results are only available for one hour after cost estimation task is done.

    Args:
        id (str):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
]:
    """Retrieve an order estimation task

     Retrieve an order cost estimation task from a specific store.
    Estimation results are only available for one hour after cost estimation task is done.

    Args:
        id (str):
        x_pf_store_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOrderEstimationTaskResponse200, GetOrderEstimationTaskResponse401, GetOrderEstimationTaskResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
