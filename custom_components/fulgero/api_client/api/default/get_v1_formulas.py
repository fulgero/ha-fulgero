import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.formulas_response import FormulasResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date: str | Unset = UNSET
    if not isinstance(date, Unset):
        json_date = date.isoformat()
    params["date"] = json_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/formulas",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | FormulasResponse:
    if response.status_code == 200:
        response_200 = FormulasResponse.from_dict(response.json())

        return response_200

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | FormulasResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
) -> Response[ApiError | FormulasResponse]:
    """Public catalogue of modeled supplier offers

    Args:
        date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | FormulasResponse]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
) -> ApiError | FormulasResponse | None:
    """Public catalogue of modeled supplier offers

    Args:
        date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | FormulasResponse
    """

    return sync_detailed(
        client=client,
        date=date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
) -> Response[ApiError | FormulasResponse]:
    """Public catalogue of modeled supplier offers

    Args:
        date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | FormulasResponse]
    """

    kwargs = _get_kwargs(
        date=date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.date | Unset = UNSET,
) -> ApiError | FormulasResponse | None:
    """Public catalogue of modeled supplier offers

    Args:
        date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | FormulasResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
        )
    ).parsed
