"""Data update coordinator: today's (and, once published, tomorrow's) retail prices."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api_client.api.default import get_v1_prices_retail
from .api_client.client import AuthenticatedClient
from .api_client.models import ApiError, RetailDayResponse
from .const import UPDATE_INTERVAL_MINUTES

_LOGGER = logging.getLogger(__name__)

RO_TZ = ZoneInfo("Europe/Bucharest")


@dataclass
class FulgeroData:
    """Today's response, tomorrow's (None until published), and shared meta."""

    today: RetailDayResponse
    tomorrow: RetailDayResponse | None


class FulgeroCoordinator(DataUpdateCoordinator[FulgeroData]):
    """Fetches the retail price curve through the generated OpenAPI client (the only API path)."""

    def __init__(
        self,
        hass: HomeAssistant,
        client: AuthenticatedClient,
        zone: str,
        formula: str,
        voltage: str,
        vat: str,
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=f"fulgero {zone}/{formula}",
            update_interval=timedelta(minutes=UPDATE_INTERVAL_MINUTES),
        )
        self._client = client
        self._zone = zone
        self._formula = formula
        self._voltage = voltage
        self._vat = vat

    async def async_close(self) -> None:
        """Close the entry-scoped connection pool (called on unload)."""
        await self._client.get_async_httpx_client().aclose()

    async def _async_update_data(self) -> FulgeroData:
        # Delivery days are Bucharest calendar days regardless of the HA host's timezone.
        today_ro = datetime.now(RO_TZ).date()
        today = await self._fetch(today_ro)
        if today is None:
            raise UpdateFailed(f"no retail prices for {today_ro} (zone {self._zone})")
        # Tomorrow is not published until early afternoon — absence is normal, never an error.
        tomorrow = await self._fetch(today_ro + timedelta(days=1))
        return FulgeroData(today=today, tomorrow=tomorrow)

    async def _fetch(self, day: date) -> RetailDayResponse | None:
        try:
            result = await get_v1_prices_retail.asyncio(
                client=self._client,
                date=day,
                zone=self._zone,
                formula=self._formula,
                voltage=self._voltage,
                vat=self._vat,
            )
        except Exception as err:  # httpx transport errors
            raise UpdateFailed(f"Fulgero API request failed: {err}") from err
        if isinstance(result, RetailDayResponse):
            return result
        if isinstance(result, ApiError):
            # not_published_yet (a 404 with Retry-After) is the normal pre-publication answer.
            if result.type_ == "not_published_yet":
                return None
            raise UpdateFailed(f"Fulgero API error for {day}: {result.type_} — {result.detail}")
        return None
