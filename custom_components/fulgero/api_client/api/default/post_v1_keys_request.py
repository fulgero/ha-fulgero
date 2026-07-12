from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.key_request_accepted import KeyRequestAccepted
from ...models.key_request_body import KeyRequestBody
from ...types import Response


def _get_kwargs(
    *,
    body: KeyRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/keys/request",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | KeyRequestAccepted:
    if response.status_code == 202:
        response_202 = KeyRequestAccepted.from_dict(response.json())

        return response_202

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | KeyRequestAccepted]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequestBody,
) -> Response[ApiError | KeyRequestAccepted]:
    """Request an API key by email; a verification link is emailed

     Always returns 202 for a well-formed request, whether or not the email is already known (no account
    enumeration). The key is revealed only on the /verify page the email links to.

    Args:
        body (KeyRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | KeyRequestAccepted]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequestBody,
) -> ApiError | KeyRequestAccepted | None:
    """Request an API key by email; a verification link is emailed

     Always returns 202 for a well-formed request, whether or not the email is already known (no account
    enumeration). The key is revealed only on the /verify page the email links to.

    Args:
        body (KeyRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | KeyRequestAccepted
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequestBody,
) -> Response[ApiError | KeyRequestAccepted]:
    """Request an API key by email; a verification link is emailed

     Always returns 202 for a well-formed request, whether or not the email is already known (no account
    enumeration). The key is revealed only on the /verify page the email links to.

    Args:
        body (KeyRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | KeyRequestAccepted]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: KeyRequestBody,
) -> ApiError | KeyRequestAccepted | None:
    """Request an API key by email; a verification link is emailed

     Always returns 202 for a well-formed request, whether or not the email is already known (no account
    enumeration). The key is revealed only on the /verify page the email links to.

    Args:
        body (KeyRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | KeyRequestAccepted
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
