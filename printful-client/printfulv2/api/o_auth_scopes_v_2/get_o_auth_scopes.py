from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_o_auth_scopes_response_200 import GetOAuthScopesResponse200
from ...models.get_o_auth_scopes_response_401 import GetOAuthScopesResponse401
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/oauth-scopes",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]:
    if response.status_code == 200:
        response_200 = GetOAuthScopesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GetOAuthScopesResponse401.from_dict(response.json())

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]:
    """Retrieve OAuth scopes

     This endpoint will retrieve all OAuth scopes associated with the used token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]:
    """Retrieve OAuth scopes

     This endpoint will retrieve all OAuth scopes associated with the used token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]:
    """Retrieve OAuth scopes

     This endpoint will retrieve all OAuth scopes associated with the used token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]]:
    """Retrieve OAuth scopes

     This endpoint will retrieve all OAuth scopes associated with the used token

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetOAuthScopesResponse200, GetOAuthScopesResponse401]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
