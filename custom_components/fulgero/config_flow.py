"""Config flow: base URL + API key, then zone/formula pickers populated from the live API."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.helpers.selector import (
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
)

from .api_client.api.default import get_v1_formulas, get_v1_zones
from .api_client.models import FormulasResponse, ZonesResponse
from .const import (
    CONF_API_KEY,
    CONF_BASE_URL,
    CONF_FORMULA,
    CONF_VAT,
    CONF_VOLTAGE,
    CONF_ZONE,
    DEFAULT_BASE_URL,
    DEFAULT_VAT,
    DEFAULT_VOLTAGE,
    DOMAIN,
    VAT_MODES,
    VOLTAGES,
)

_LOGGER = logging.getLogger(__name__)

STEP_USER = vol.Schema(
    {
        vol.Required(CONF_BASE_URL, default=DEFAULT_BASE_URL): str,
        vol.Required(CONF_API_KEY): str,
    }
)


class FulgeroConfigFlow(ConfigFlow, domain=DOMAIN):
    """Two steps: credentials (validated by listing zones), then zone/offer/voltage/VAT."""

    VERSION = 1

    def __init__(self) -> None:
        self._base_url: str = DEFAULT_BASE_URL
        self._api_key: str = ""
        self._zones: list[SelectOptionDict] = []
        self._formulas: list[SelectOptionDict] = []

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        errors: dict[str, str] = {}
        if user_input is not None:
            self._base_url = user_input[CONF_BASE_URL].rstrip("/")
            self._api_key = user_input[CONF_API_KEY].strip()
            try:
                await self._load_options()
            except Exception:  # noqa: BLE001 — any failure means "can't reach/authenticate"
                _LOGGER.exception("Fulgero credential validation failed")
                errors["base"] = "cannot_connect"
            if not errors and not self._zones:
                errors["base"] = "invalid_auth"
            # zones OK but no offers: the target step's Required offer picker would be
            # unsubmittable with zero options — surface it here instead of a dead-end form.
            if not errors and not self._formulas:
                errors["base"] = "empty_catalog"
            if not errors:
                return await self.async_step_target()
        return self.async_show_form(step_id="user", data_schema=STEP_USER, errors=errors)

    async def async_step_target(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        if user_input is not None:
            await self.async_set_unique_id(
                f"{user_input[CONF_ZONE]}-{user_input[CONF_FORMULA]}"
                f"-{user_input[CONF_VOLTAGE]}-{user_input[CONF_VAT]}"
            )
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=f"Fulgero {user_input[CONF_ZONE]} · {user_input[CONF_FORMULA]}",
                data={
                    CONF_BASE_URL: self._base_url,
                    CONF_API_KEY: self._api_key,
                    **user_input,
                },
            )
        schema = vol.Schema(
            {
                vol.Required(CONF_ZONE): SelectSelector(
                    SelectSelectorConfig(options=self._zones)
                ),
                vol.Required(CONF_FORMULA): SelectSelector(
                    SelectSelectorConfig(options=self._formulas)
                ),
                vol.Required(CONF_VOLTAGE, default=DEFAULT_VOLTAGE): vol.In(VOLTAGES),
                vol.Required(CONF_VAT, default=DEFAULT_VAT): vol.In(VAT_MODES),
            }
        )
        return self.async_show_form(step_id="target", data_schema=schema)

    async def _load_options(self) -> None:
        # local import avoids a circular import at HA module scan time
        from . import build_client

        client = build_client(self.hass, self._base_url, self._api_key)
        try:
            zones = await get_v1_zones.asyncio(client=client)
            formulas = await get_v1_formulas.asyncio(client=client)
        finally:
            # probe client per attempt — release its pool rather than waiting for HA shutdown
            await client.get_async_httpx_client().aclose()
        self._zones = (
            [
                SelectOptionDict(value=z.code, label=f"{z.code} — {z.name} ({z.operator})")
                for z in zones.zones
            ]
            if isinstance(zones, ZonesResponse) and zones.zones
            else []
        )
        self._formulas = (
            [
                SelectOptionDict(value=f.offer_id, label=f"{f.offer_id} — {f.offer_name}")
                for f in formulas.formulas
            ]
            if isinstance(formulas, FormulasResponse) and formulas.formulas
            else []
        )
