from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.map_big_decimal import MapBigDecimal


T = TypeVar("T", bound="RetailInterval")


@_attrs_define
class RetailInterval:
    """
    Attributes:
        start (datetime.datetime):
        resolution (str):
        total (float):
        components (MapBigDecimal):
    """

    start: datetime.datetime
    resolution: str
    total: float
    components: MapBigDecimal
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.isoformat()

        resolution = self.resolution

        total = self.total

        components = self.components.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "resolution": resolution,
                "total": total,
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_big_decimal import MapBigDecimal

        d = dict(src_dict)
        start = datetime.datetime.fromisoformat(d.pop("start"))

        resolution = d.pop("resolution")

        total = d.pop("total")

        components = MapBigDecimal.from_dict(d.pop("components"))

        retail_interval = cls(
            start=start,
            resolution=resolution,
            total=total,
            components=components,
        )

        retail_interval.additional_properties = d
        return retail_interval

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
