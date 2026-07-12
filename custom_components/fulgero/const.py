"""Constants for the Fulgero integration."""

DOMAIN = "fulgero"

CONF_BASE_URL = "base_url"
CONF_API_KEY = "api_key"
CONF_ZONE = "zone"
CONF_FORMULA = "formula"
CONF_VOLTAGE = "voltage"
CONF_VAT = "vat"

DEFAULT_BASE_URL = "https://api.fulgero.ro"
DEFAULT_VOLTAGE = "JT"
DEFAULT_VAT = "include"

VOLTAGES = ["JT", "MT", "IT"]
VAT_MODES = ["include", "exclude"]

# The API serves next-day prices by ~15:00 Bucharest; refreshing every 30 minutes keeps today's
# (immutable, CDN-cached) data warm and picks tomorrow's up shortly after publication without
# hammering the origin (responses are CDN-cached; the key exists for origin protection).
UPDATE_INTERVAL_MINUTES = 30

ATTRIBUTION_FALLBACK = (
    "Spot: ENTSO-E Transparency Platform (CC-BY 4.0) · FX: BNR · Tariffs: ANRE"
)
