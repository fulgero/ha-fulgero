from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Sources")


@_attrs_define
class Sources:
    """
    Attributes:
        entsoe_last (datetime.datetime | Unset):
        bnr_last (datetime.datetime | Unset):
        tariffs_last (datetime.datetime | Unset):
    """

    entsoe_last: datetime.datetime | Unset = UNSET
    bnr_last: datetime.datetime | Unset = UNSET
    tariffs_last: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entsoe_last: str | Unset = UNSET
        if not isinstance(self.entsoe_last, Unset):
            entsoe_last = self.entsoe_last.isoformat()

        bnr_last: str | Unset = UNSET
        if not isinstance(self.bnr_last, Unset):
            bnr_last = self.bnr_last.isoformat()

        tariffs_last: str | Unset = UNSET
        if not isinstance(self.tariffs_last, Unset):
            tariffs_last = self.tariffs_last.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entsoe_last is not UNSET:
            field_dict["entsoe_last"] = entsoe_last
        if bnr_last is not UNSET:
            field_dict["bnr_last"] = bnr_last
        if tariffs_last is not UNSET:
            field_dict["tariffs_last"] = tariffs_last

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _entsoe_last = d.pop("entsoe_last", UNSET)
        entsoe_last: datetime.datetime | Unset
        if isinstance(_entsoe_last, Unset):
            entsoe_last = UNSET
        else:
            entsoe_last = datetime.datetime.fromisoformat(_entsoe_last)

        _bnr_last = d.pop("bnr_last", UNSET)
        bnr_last: datetime.datetime | Unset
        if isinstance(_bnr_last, Unset):
            bnr_last = UNSET
        else:
            bnr_last = datetime.datetime.fromisoformat(_bnr_last)

        _tariffs_last = d.pop("tariffs_last", UNSET)
        tariffs_last: datetime.datetime | Unset
        if isinstance(_tariffs_last, Unset):
            tariffs_last = UNSET
        else:
            tariffs_last = datetime.datetime.fromisoformat(_tariffs_last)

        sources = cls(
            entsoe_last=entsoe_last,
            bnr_last=bnr_last,
            tariffs_last=tariffs_last,
        )

        sources.additional_properties = d
        return sources

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
