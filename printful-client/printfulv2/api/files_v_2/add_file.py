from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_file_response_400 import AddFileResponse400
from ...models.add_file_response_404 import AddFileResponse404
from ...models.file import File
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: File,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_pf_store_id, Unset):
        headers["X-PF-Store-Id"] = x_pf_store_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/files",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddFileResponse400, AddFileResponse404]]:
    if response.status_code == 400:
        response_400 = AddFileResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = AddFileResponse404.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AddFileResponse400, AddFileResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: File,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[AddFileResponse400, AddFileResponse404]]:
    """Add a new file

     Adds a new File to the library by providing URL of the file.

    If a file with identical URL already exists, then the original file is returned. If a file does not
    exist, a new file is created.

    [See examples](#tag/Examples/File-Library-API-examples/Add-a-new-file)

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (File): Information about the added File

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddFileResponse400, AddFileResponse404]]
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
    body: File,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[AddFileResponse400, AddFileResponse404]]:
    """Add a new file

     Adds a new File to the library by providing URL of the file.

    If a file with identical URL already exists, then the original file is returned. If a file does not
    exist, a new file is created.

    [See examples](#tag/Examples/File-Library-API-examples/Add-a-new-file)

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (File): Information about the added File

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddFileResponse400, AddFileResponse404]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_pf_store_id=x_pf_store_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: File,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Response[Union[AddFileResponse400, AddFileResponse404]]:
    """Add a new file

     Adds a new File to the library by providing URL of the file.

    If a file with identical URL already exists, then the original file is returned. If a file does not
    exist, a new file is created.

    [See examples](#tag/Examples/File-Library-API-examples/Add-a-new-file)

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (File): Information about the added File

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddFileResponse400, AddFileResponse404]]
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
    body: File,
    x_pf_store_id: Union[Unset, str] = UNSET,
) -> Optional[Union[AddFileResponse400, AddFileResponse404]]:
    """Add a new file

     Adds a new File to the library by providing URL of the file.

    If a file with identical URL already exists, then the original file is returned. If a file does not
    exist, a new file is created.

    [See examples](#tag/Examples/File-Library-API-examples/Add-a-new-file)

    Args:
        x_pf_store_id (Union[Unset, str]):
        body (File): Information about the added File

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddFileResponse400, AddFileResponse404]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_pf_store_id=x_pf_store_id,
        )
    ).parsed
