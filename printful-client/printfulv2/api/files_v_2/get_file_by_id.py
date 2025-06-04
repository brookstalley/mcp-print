from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_file_by_id_response_400 import GetFileByIdResponse400
from ...models.get_file_by_id_response_404 import GetFileByIdResponse404
from ...types import Response


def _get_kwargs(
    id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v2/files/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetFileByIdResponse400, GetFileByIdResponse404]]:
    if response.status_code == 400:
        response_400 = GetFileByIdResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = GetFileByIdResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetFileByIdResponse400, GetFileByIdResponse404]]:
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
) -> Response[Union[GetFileByIdResponse400, GetFileByIdResponse404]]:
    """Retrieve a single file from the file library

     Get basic information about the file stored in the file library

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetFileByIdResponse400, GetFileByIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetFileByIdResponse400, GetFileByIdResponse404]]:
    """Retrieve a single file from the file library

     Get basic information about the file stored in the file library

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetFileByIdResponse400, GetFileByIdResponse404]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetFileByIdResponse400, GetFileByIdResponse404]]:
    """Retrieve a single file from the file library

     Get basic information about the file stored in the file library

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetFileByIdResponse400, GetFileByIdResponse404]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetFileByIdResponse400, GetFileByIdResponse404]]:
    """Retrieve a single file from the file library

     Get basic information about the file stored in the file library

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetFileByIdResponse400, GetFileByIdResponse404]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
