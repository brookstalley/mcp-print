from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_mockup_generator_tasks_response_200 import GetMockupGeneratorTasksResponse200
from ...models.get_mockup_generator_tasks_response_400 import GetMockupGeneratorTasksResponse400
from ...models.get_mockup_generator_tasks_response_401 import GetMockupGeneratorTasksResponse401
from ...models.get_mockup_generator_tasks_response_404 import GetMockupGeneratorTasksResponse404
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: list[str],
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_id = id

    params["id"] = json_id

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/mockup-tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetMockupGeneratorTasksResponse200,
        GetMockupGeneratorTasksResponse400,
        GetMockupGeneratorTasksResponse401,
        GetMockupGeneratorTasksResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = GetMockupGeneratorTasksResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetMockupGeneratorTasksResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetMockupGeneratorTasksResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = GetMockupGeneratorTasksResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetMockupGeneratorTasksResponse200,
        GetMockupGeneratorTasksResponse400,
        GetMockupGeneratorTasksResponse401,
        GetMockupGeneratorTasksResponse404,
    ]
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
    id: list[str],
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
) -> Response[
    Union[
        GetMockupGeneratorTasksResponse200,
        GetMockupGeneratorTasksResponse400,
        GetMockupGeneratorTasksResponse401,
        GetMockupGeneratorTasksResponse404,
    ]
]:
    """Retrieve Mockup Generator tasks

     Returns result of Mockup Generator tasks

    Args:
        id (list[str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMockupGeneratorTasksResponse200, GetMockupGeneratorTasksResponse400, GetMockupGeneratorTasksResponse401, GetMockupGeneratorTasksResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: list[str],
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
) -> Optional[
    Union[
        GetMockupGeneratorTasksResponse200,
        GetMockupGeneratorTasksResponse400,
        GetMockupGeneratorTasksResponse401,
        GetMockupGeneratorTasksResponse404,
    ]
]:
    """Retrieve Mockup Generator tasks

     Returns result of Mockup Generator tasks

    Args:
        id (list[str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetMockupGeneratorTasksResponse200, GetMockupGeneratorTasksResponse400, GetMockupGeneratorTasksResponse401, GetMockupGeneratorTasksResponse404]
    """

    return sync_detailed(
        client=client,
        id=id,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: list[str],
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
) -> Response[
    Union[
        GetMockupGeneratorTasksResponse200,
        GetMockupGeneratorTasksResponse400,
        GetMockupGeneratorTasksResponse401,
        GetMockupGeneratorTasksResponse404,
    ]
]:
    """Retrieve Mockup Generator tasks

     Returns result of Mockup Generator tasks

    Args:
        id (list[str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetMockupGeneratorTasksResponse200, GetMockupGeneratorTasksResponse400, GetMockupGeneratorTasksResponse401, GetMockupGeneratorTasksResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: list[str],
    limit: Union[Unset, int] = 20,
    offset: Union[Unset, int] = 0,
) -> Optional[
    Union[
        GetMockupGeneratorTasksResponse200,
        GetMockupGeneratorTasksResponse400,
        GetMockupGeneratorTasksResponse401,
        GetMockupGeneratorTasksResponse404,
    ]
]:
    """Retrieve Mockup Generator tasks

     Returns result of Mockup Generator tasks

    Args:
        id (list[str]):
        limit (Union[Unset, int]):  Default: 20.
        offset (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetMockupGeneratorTasksResponse200, GetMockupGeneratorTasksResponse400, GetMockupGeneratorTasksResponse401, GetMockupGeneratorTasksResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            limit=limit,
            offset=offset,
        )
    ).parsed
