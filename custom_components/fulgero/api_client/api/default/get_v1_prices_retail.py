import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.retail_day_response import RetailDayResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date,
    zone: str,
    formula: str,
    vat: str | Unset = "include",
    voltage: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    params["zone"] = zone

    params["formula"] = formula

    params["vat"] = vat

    params["voltage"] = voltage

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/prices/retail",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | RetailDayResponse:
    if response.status_code == 200:
        response_200 = RetailDayResponse.from_dict(response.json())

        return response_200

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | RetailDayResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    zone: str,
    formula: str,
    vat: str | Unset = "include",
    voltage: str | Unset = UNSET,
) -> Response[ApiError | RetailDayResponse]:
    """All-in per-interval retail price for a day/zone/formula

    Args:
        date (datetime.date):
        zone (str):
        formula (str):
        vat (str | Unset):  Default: 'include'.
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | RetailDayResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        zone=zone,
        formula=formula,
        vat=vat,
        voltage=voltage,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    zone: str,
    formula: str,
    vat: str | Unset = "include",
    voltage: str | Unset = UNSET,
) -> ApiError | RetailDayResponse | None:
    """All-in per-interval retail price for a day/zone/formula

    Args:
        date (datetime.date):
        zone (str):
        formula (str):
        vat (str | Unset):  Default: 'include'.
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | RetailDayResponse
    """

    return sync_detailed(
        client=client,
        date=date,
        zone=zone,
        formula=formula,
        vat=vat,
        voltage=voltage,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    zone: str,
    formula: str,
    vat: str | Unset = "include",
    voltage: str | Unset = UNSET,
) -> Response[ApiError | RetailDayResponse]:
    """All-in per-interval retail price for a day/zone/formula

    Args:
        date (datetime.date):
        zone (str):
        formula (str):
        vat (str | Unset):  Default: 'include'.
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | RetailDayResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        zone=zone,
        formula=formula,
        vat=vat,
        voltage=voltage,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    zone: str,
    formula: str,
    vat: str | Unset = "include",
    voltage: str | Unset = UNSET,
) -> ApiError | RetailDayResponse | None:
    """All-in per-interval retail price for a day/zone/formula

    Args:
        date (datetime.date):
        zone (str):
        formula (str):
        vat (str | Unset):  Default: 'include'.
        voltage (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | RetailDayResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            zone=zone,
            formula=formula,
            vat=vat,
            voltage=voltage,
        )
    ).parsed
