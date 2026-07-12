import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.tariff_stack_response import TariffStackResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    zone: str,
    date: datetime.date,
    voltage: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["zone"] = zone

    json_date = date.isoformat()
    params["date"] = json_date

    params["voltage"] = voltage

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/tariff-stack",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | TariffStackResponse:
    if response.status_code == 200:
        response_200 = TariffStackResponse.from_dict(response.json())

        return response_200

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | TariffStackResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    zone: str,
    date: datetime.date,
    voltage: str | Unset = UNSET,
) -> Response[ApiError | TariffStackResponse]:
    """Regulated component breakdown for a zone/date

    Args:
        zone (str):
        date (datetime.date):
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TariffStackResponse]
    """

    kwargs = _get_kwargs(
        zone=zone,
        date=date,
        voltage=voltage,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    zone: str,
    date: datetime.date,
    voltage: str | Unset = UNSET,
) -> ApiError | TariffStackResponse | None:
    """Regulated component breakdown for a zone/date

    Args:
        zone (str):
        date (datetime.date):
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TariffStackResponse
    """

    return sync_detailed(
        client=client,
        zone=zone,
        date=date,
        voltage=voltage,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    zone: str,
    date: datetime.date,
    voltage: str | Unset = UNSET,
) -> Response[ApiError | TariffStackResponse]:
    """Regulated component breakdown for a zone/date

    Args:
        zone (str):
        date (datetime.date):
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | TariffStackResponse]
    """

    kwargs = _get_kwargs(
        zone=zone,
        date=date,
        voltage=voltage,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    zone: str,
    date: datetime.date,
    voltage: str | Unset = UNSET,
) -> ApiError | TariffStackResponse | None:
    """Regulated component breakdown for a zone/date

    Args:
        zone (str):
        date (datetime.date):
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | TariffStackResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            zone=zone,
            date=date,
            voltage=voltage,
        )
    ).parsed
