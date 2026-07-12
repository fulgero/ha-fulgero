from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DayAheadInterval")


@_attrs_define
class DayAheadInterval:
    """
    Attributes:
        start (datetime.datetime):
        resolution (str):
        price_eur_mwh (float):
        price_ron_kwh (float | Unset):
    """

    start: datetime.datetime
    resolution: str
    price_eur_mwh: float
    price_ron_kwh: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start.isoformat()

        resolution = self.resolution

        price_eur_mwh = self.price_eur_mwh

        price_ron_kwh = self.price_ron_kwh

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "resolution": resolution,
                "price_eur_mwh": price_eur_mwh,
            }
        )
        if price_ron_kwh is not UNSET:
            field_dict["price_ron_kwh"] = price_ron_kwh

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        start = datetime.datetime.fromisoformat(d.pop("start"))

        resolution = d.pop("resolution")

        price_eur_mwh = d.pop("price_eur_mwh")

        price_ron_kwh = d.pop("price_ron_kwh", UNSET)

        day_ahead_interval = cls(
            start=start,
            resolution=resolution,
            price_eur_mwh=price_eur_mwh,
            price_ron_kwh=price_ron_kwh,
        )

        day_ahead_interval.additional_properties = d
        return day_ahead_interval

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
