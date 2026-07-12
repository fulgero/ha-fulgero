# Fulgero — Home Assistant integration

All-in Romanian retail electricity prices in Home Assistant: day-ahead PZU spot plus the full
regulated tariff stack (distribution by DSO zone, transport, system services, cogeneration, green
certificates, CfD, excise, VAT) — per supplier offer and voltage level, in RON/kWh, from the
[Fulgero API](https://fulgero.ro).

## Installation

**HACS (custom repository):**

1. HACS → *⋮* → *Custom repositories* → add `https://github.com/fulgero/ha-fulgero`,
   category *Integration*.
2. Install **Fulgero**, restart Home Assistant.

**Manual:** copy `custom_components/fulgero/` into your `config/custom_components/` and restart.

## Configuration

*Settings → Devices & services → Add integration → Fulgero*:

1. **Account** — API base URL (default `https://api.fulgero.ro`) and your API key. Keys are
   free and self-serve at [fulgero.ro](https://fulgero.ro) (email verification; the key is shown
   exactly once).
2. **Connection point** — your distribution zone (it's on your invoice; the picker lists all 8
   Romanian DSO zones live from the API), the supplier offer (includes `PZU_RAW` — pure spot +
   regulated stack), voltage level (households: `JT`) and VAT mode.

Multiple entries are supported (e.g. compare two suppliers side by side).

## Entities

| entity | state | attributes |
|---|---|---|
| `sensor.<name>_current_price` | all-in RON/kWh for the interval covering *now* | `prices_today` / `prices_tomorrow` (`[{start, price}]`), `tomorrow_published`, `provisional`, `attribution`, `tariffs_rev` |
| `sensor.<name>_next_hour_price` | same, one hour ahead | same |

Tomorrow's curve appears when the day-ahead market data lands (afternoon/evening, Romanian time).
The `prices_today`/`prices_tomorrow` attributes are ready for template sensors, ApexCharts cards,
and cheapest-window automations.

Data sources: ENTSO-E Transparency Platform (CC-BY 4.0) · BNR · ANRE — the `attribution`
attribute carries the required notice.

## How it's built

The integration talks to the API **only** through `custom_components/fulgero/api_client/` — a
Python client generated from the service's committed OpenAPI spec (the spec is the contract; the
client is regenerated and diff-gated in the service's CI, then released here). Please don't edit
`api_client/` by hand — changes belong in the source repository's spec/pipeline.

Issues and feature requests: <https://github.com/fulgero/ha-fulgero/issues>.
