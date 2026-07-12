"""Sensors: the all-in retail price now / next hour, with full day curves as attributes."""

from __future__ import annotations

import logging
from datetime import datetime, timedelta
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.event import async_track_time_change
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.util import dt as dt_util

from . import FulgeroConfigEntry
from .api_client.models import RetailDayResponse, RetailInterval
from .api_client.types import Unset
from .const import ATTRIBUTION_FALLBACK, DOMAIN
from .coordinator import FulgeroCoordinator, FulgeroData

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: FulgeroConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator = entry.runtime_data
    async_add_entities(
        [
            FulgeroPriceSensor(coordinator, entry, offset_hours=0),
            FulgeroPriceSensor(coordinator, entry, offset_hours=1),
        ]
    )


def _intervals(day: RetailDayResponse | None) -> list[RetailInterval]:
    if day is None or isinstance(day.intervals, Unset) or day.intervals is None:
        return []
    return list(day.intervals)


def _interval_at(data: FulgeroData, at: datetime) -> RetailInterval | None:
    """The interval covering `at` — per-interval resolution (the MTU-switch day is self-describing)."""
    for iv in _intervals(data.today) + _intervals(data.tomorrow):
        minutes = 15 if iv.resolution == "PT15M" else 60
        if iv.start <= at < iv.start + timedelta(minutes=minutes):
            return iv
    return None


def _curve(day: RetailDayResponse | None) -> list[dict[str, Any]]:
    return [
        {"start": iv.start.isoformat(), "price": iv.total} for iv in _intervals(day)
    ]


class FulgeroPriceSensor(CoordinatorEntity[FulgeroCoordinator], SensorEntity):
    """All-in RON/kWh now (offset 0) or one hour ahead (offset 1)."""

    _attr_has_entity_name = True
    _attr_native_unit_of_measurement = "RON/kWh"
    # deliberately NO state_class: long-term mean/min/max statistics of a stepping tariff are
    # meaningless (the Nordpool-style convention for price sensors)
    _attr_suggested_display_precision = 4

    def __init__(
        self,
        coordinator: FulgeroCoordinator,
        entry: FulgeroConfigEntry,
        offset_hours: int,
    ) -> None:
        super().__init__(coordinator)
        self._offset = timedelta(hours=offset_hours)
        key = "current_price" if offset_hours == 0 else "next_hour_price"
        self._attr_translation_key = key
        self._attr_unique_id = f"{entry.entry_id}-{key}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=entry.title,
            entry_type=DeviceEntryType.SERVICE,
            manufacturer="Fulgero",
            configuration_url="https://fulgero.ro",
        )

    async def async_added_to_hass(self) -> None:
        await super().async_added_to_hass()
        # Interval boundaries pass without a coordinator refresh — re-render on each quarter hour.
        self.async_on_remove(
            async_track_time_change(
                self.hass, self._boundary, minute=[0, 15, 30, 45], second=5
            )
        )

    @callback
    def _boundary(self, _now: datetime) -> None:
        self.async_write_ha_state()

    @property
    def native_value(self) -> float | None:
        iv = _interval_at(self.coordinator.data, dt_util.utcnow() + self._offset)
        return iv.total if iv else None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        data = self.coordinator.data
        meta = data.today.meta
        return {
            "prices_today": _curve(data.today),
            "prices_tomorrow": _curve(data.tomorrow),
            "tomorrow_published": data.tomorrow is not None,
            "provisional": meta.provisional,
            "unit": data.today.unit,
            "vat": data.today.vat,
            "attribution": meta.attribution or ATTRIBUTION_FALLBACK,
            "tariffs_rev": None if isinstance(meta.tariffs_rev, Unset) else meta.tariffs_rev,
        }
