from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_meta import ApiMeta
    from ..models.day_ahead_interval import DayAheadInterval


T = TypeVar("T", bound="DayAheadResponse")


@_attrs_define
class DayAheadResponse:
    """
    Attributes:
        date (datetime.date):
        zone (str):
        meta (ApiMeta):
        intervals (list[DayAheadInterval] | Unset):
    """

    date: datetime.date
    zone: str
    meta: ApiMeta
    intervals: list[DayAheadInterval] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        zone = self.zone

        meta = self.meta.to_dict()

        intervals: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.intervals, Unset):
            intervals = []
            for intervals_item_data in self.intervals:
                intervals_item = intervals_item_data.to_dict()
                intervals.append(intervals_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "zone": zone,
                "meta": meta,
            }
        )
        if intervals is not UNSET:
            field_dict["intervals"] = intervals

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meta import ApiMeta
        from ..models.day_ahead_interval import DayAheadInterval

        d = dict(src_dict)
        date = datetime.date.fromisoformat(d.pop("date"))

        zone = d.pop("zone")

        meta = ApiMeta.from_dict(d.pop("meta"))

        _intervals = d.pop("intervals", UNSET)
        intervals: list[DayAheadInterval] | Unset = UNSET
        if _intervals is not UNSET:
            intervals = []
            for intervals_item_data in _intervals:
                intervals_item = DayAheadInterval.from_dict(intervals_item_data)

                intervals.append(intervals_item)

        day_ahead_response = cls(
            date=date,
            zone=zone,
            meta=meta,
            intervals=intervals,
        )

        day_ahead_response.additional_properties = d
        return day_ahead_response

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
