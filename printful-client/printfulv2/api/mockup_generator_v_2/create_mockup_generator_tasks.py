from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_mockup_generator_tasks_response_200 import CreateMockupGeneratorTasksResponse200
from ...models.create_mockup_generator_tasks_response_400 import CreateMockupGeneratorTasksResponse400
from ...models.create_mockup_generator_tasks_response_401 import CreateMockupGeneratorTasksResponse401
from ...models.create_mockup_generator_tasks_response_404 import CreateMockupGeneratorTasksResponse404
from ...models.mockup_task_creation import MockupTaskCreation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: MockupTaskCreation,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/mockup-tasks",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateMockupGeneratorTasksResponse200,
        CreateMockupGeneratorTasksResponse400,
        CreateMockupGeneratorTasksResponse401,
        CreateMockupGeneratorTasksResponse404,
    ]
]:
    if response.status_code == 200:
        response_200 = CreateMockupGeneratorTasksResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = CreateMockupGeneratorTasksResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateMockupGeneratorTasksResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = CreateMockupGeneratorTasksResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateMockupGeneratorTasksResponse200,
        CreateMockupGeneratorTasksResponse400,
        CreateMockupGeneratorTasksResponse401,
        CreateMockupGeneratorTasksResponse404,
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
    body: MockupTaskCreation,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        CreateMockupGeneratorTasksResponse200,
        CreateMockupGeneratorTasksResponse400,
        CreateMockupGeneratorTasksResponse401,
        CreateMockupGeneratorTasksResponse404,
    ]
]:
    """Create Mockup Generator tasks

     Create Mockup Generator tasks

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (MockupTaskCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateMockupGeneratorTasksResponse200, CreateMockupGeneratorTasksResponse400, CreateMockupGeneratorTasksResponse401, CreateMockupGeneratorTasksResponse404]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_pf_store_id=x_pf_store_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: MockupTaskCreation,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        CreateMockupGeneratorTasksResponse200,
        CreateMockupGeneratorTasksResponse400,
        CreateMockupGeneratorTasksResponse401,
        CreateMockupGeneratorTasksResponse404,
    ]
]:
    """Create Mockup Generator tasks

     Create Mockup Generator tasks

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (MockupTaskCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateMockupGeneratorTasksResponse200, CreateMockupGeneratorTasksResponse400, CreateMockupGeneratorTasksResponse401, CreateMockupGeneratorTasksResponse404]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: MockupTaskCreation,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        CreateMockupGeneratorTasksResponse200,
        CreateMockupGeneratorTasksResponse400,
        CreateMockupGeneratorTasksResponse401,
        CreateMockupGeneratorTasksResponse404,
    ]
]:
    """Create Mockup Generator tasks

     Create Mockup Generator tasks

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (MockupTaskCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateMockupGeneratorTasksResponse200, CreateMockupGeneratorTasksResponse400, CreateMockupGeneratorTasksResponse401, CreateMockupGeneratorTasksResponse404]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_pf_store_id=x_pf_store_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: MockupTaskCreation,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        CreateMockupGeneratorTasksResponse200,
        CreateMockupGeneratorTasksResponse400,
        CreateMockupGeneratorTasksResponse401,
        CreateMockupGeneratorTasksResponse404,
    ]
]:
    """Create Mockup Generator tasks

     Create Mockup Generator tasks

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (MockupTaskCreation):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateMockupGeneratorTasksResponse200, CreateMockupGeneratorTasksResponse400, CreateMockupGeneratorTasksResponse401, CreateMockupGeneratorTasksResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
