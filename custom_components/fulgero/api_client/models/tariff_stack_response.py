from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.api_meta import ApiMeta
    from ..models.map_big_decimal import MapBigDecimal


T = TypeVar("T", bound="TariffStackResponse")


@_attrs_define
class TariffStackResponse:
    """
    Attributes:
        zone (str):
        voltage (str):
        date (datetime.date):
        components (MapBigDecimal):
        vat_rate (float):
        meta (ApiMeta):
    """

    zone: str
    voltage: str
    date: datetime.date
    components: MapBigDecimal
    vat_rate: float
    meta: ApiMeta
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone = self.zone

        voltage = self.voltage

        date = self.date.isoformat()

        components = self.components.to_dict()

        vat_rate = self.vat_rate

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "zone": zone,
                "voltage": voltage,
                "date": date,
                "components": components,
                "vat_rate": vat_rate,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meta import ApiMeta
        from ..models.map_big_decimal import MapBigDecimal

        d = dict(src_dict)
        zone = d.pop("zone")

        voltage = d.pop("voltage")

        date = datetime.date.fromisoformat(d.pop("date"))

        components = MapBigDecimal.from_dict(d.pop("components"))

        vat_rate = d.pop("vat_rate")

        meta = ApiMeta.from_dict(d.pop("meta"))

        tariff_stack_response = cls(
            zone=zone,
            voltage=voltage,
            date=date,
            components=components,
            vat_rate=vat_rate,
            meta=meta,
        )

        tariff_stack_response.additional_properties = d
        return tariff_stack_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
