from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ZoneInfo")


@_attrs_define
class ZoneInfo:
    """
    Attributes:
        code (str):
        operator (str):
        name (str):
        counties (list[str] | Unset):
    """

    code: str
    operator: str
    name: str
    counties: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        operator = self.operator

        name = self.name

        counties: list[str] | Unset = UNSET
        if not isinstance(self.counties, Unset):
            counties = self.counties

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "operator": operator,
                "name": name,
            }
        )
        if counties is not UNSET:
            field_dict["counties"] = counties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        operator = d.pop("operator")

        name = d.pop("name")

        counties = cast(list[str], d.pop("counties", UNSET))

        zone_info = cls(
            code=code,
            operator=operator,
            name=name,
            counties=counties,
        )

        zone_info.additional_properties = d
        return zone_info

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
