"""Fulgero — Romanian all-in retail electricity prices (fulgero.ro).

The integration consumes ONLY the generated OpenAPI client vendored under `api_client/`
(the OpenAPI spec is the contract between the Fulgero service and this component; the client is
regenerated in CI whenever the spec changes — never edit `api_client/` by hand).
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.httpx_client import create_async_httpx_client

from .api_client.client import AuthenticatedClient
from .const import (
    CONF_API_KEY,
    CONF_BASE_URL,
    CONF_FORMULA,
    CONF_VAT,
    CONF_VOLTAGE,
    CONF_ZONE,
    DEFAULT_VAT,
    DEFAULT_VOLTAGE,
    DOMAIN,
)
from .coordinator import FulgeroCoordinator

PLATFORMS = [Platform.SENSOR]

type FulgeroConfigEntry = ConfigEntry[FulgeroCoordinator]


def build_client(hass: HomeAssistant, base_url: str, api_key: str) -> AuthenticatedClient:
    """The one place the API key becomes a header: X-Api-Key, no Bearer prefix (API rule D1).

    The httpx transport is created through HA's `create_async_httpx_client` — it reuses HA's
    cached SSL context (no blocking CA-bundle I/O on the event loop) and is closed by HA at
    shutdown. We inject it into the generated client, which otherwise would lazily construct
    its own `httpx.AsyncClient` inside the loop.
    """
    client = AuthenticatedClient(
        base_url=base_url,
        token=api_key,
        prefix="",
        auth_header_name="X-Api-Key",
    )
    client.set_async_httpx_client(
        create_async_httpx_client(
            hass,
            base_url=base_url,
            headers={"X-Api-Key": api_key},
        )
    )
    return client


async def async_setup_entry(hass: HomeAssistant, entry: FulgeroConfigEntry) -> bool:
    coordinator = FulgeroCoordinator(
        hass,
        build_client(hass, entry.data[CONF_BASE_URL], entry.data[CONF_API_KEY]),
        zone=entry.data[CONF_ZONE],
        formula=entry.data[CONF_FORMULA],
        voltage=entry.data.get(CONF_VOLTAGE, DEFAULT_VOLTAGE),
        vat=entry.data.get(CONF_VAT, DEFAULT_VAT),
    )
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: FulgeroConfigEntry) -> bool:
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unloaded:
        await entry.runtime_data.async_close()
    return unloaded
