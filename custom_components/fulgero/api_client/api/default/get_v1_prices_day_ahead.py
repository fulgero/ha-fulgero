import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ...client import AuthenticatedClient, Client
from ...models.api_error import ApiError
from ...models.day_ahead_response import DayAheadResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: datetime.date,
    resolution: str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date = date.isoformat()
    params["date"] = json_date

    params["resolution"] = resolution

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/prices/day-ahead",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ApiError | DayAheadResponse:
    if response.status_code == 200:
        response_200 = DayAheadResponse.from_dict(response.json())

        return response_200

    response_default = ApiError.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ApiError | DayAheadResponse]:
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
    resolution: str | Unset = UNSET,
) -> Response[ApiError | DayAheadResponse]:
    """Raw PZU day-ahead spot for the day (EUR/MWh + RON/kWh mirror)

    Args:
        date (datetime.date):
        resolution (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DayAheadResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        resolution=resolution,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    resolution: str | Unset = UNSET,
) -> ApiError | DayAheadResponse | None:
    """Raw PZU day-ahead spot for the day (EUR/MWh + RON/kWh mirror)

    Args:
        date (datetime.date):
        resolution (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DayAheadResponse
    """

    return sync_detailed(
        client=client,
        date=date,
        resolution=resolution,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    resolution: str | Unset = UNSET,
) -> Response[ApiError | DayAheadResponse]:
    """Raw PZU day-ahead spot for the day (EUR/MWh + RON/kWh mirror)

    Args:
        date (datetime.date):
        resolution (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiError | DayAheadResponse]
    """

    kwargs = _get_kwargs(
        date=date,
        resolution=resolution,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    date: datetime.date,
    resolution: str | Unset = UNSET,
) -> ApiError | DayAheadResponse | None:
    """Raw PZU day-ahead spot for the day (EUR/MWh + RON/kWh mirror)

    Args:
        date (datetime.date):
        resolution (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiError | DayAheadResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            date=date,
            resolution=resolution,
        )
    ).parsed
