from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sources import Sources


T = TypeVar("T", bound="ApiMeta")


@_attrs_define
class ApiMeta:
    """
    Attributes:
        generated_at (datetime.datetime):
        sources (Sources):
        attribution (str):
        provisional (bool):
        tariffs_rev (datetime.datetime | Unset):
    """

    generated_at: datetime.datetime
    sources: Sources
    attribution: str
    provisional: bool
    tariffs_rev: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        generated_at = self.generated_at.isoformat()

        sources = self.sources.to_dict()

        attribution = self.attribution

        provisional = self.provisional

        tariffs_rev: str | Unset = UNSET
        if not isinstance(self.tariffs_rev, Unset):
            tariffs_rev = self.tariffs_rev.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "generated_at": generated_at,
                "sources": sources,
                "attribution": attribution,
                "provisional": provisional,
            }
        )
        if tariffs_rev is not UNSET:
            field_dict["tariffs_rev"] = tariffs_rev

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources import Sources

        d = dict(src_dict)
        generated_at = datetime.datetime.fromisoformat(d.pop("generated_at"))

        sources = Sources.from_dict(d.pop("sources"))

        attribution = d.pop("attribution")

        provisional = d.pop("provisional")

        _tariffs_rev = d.pop("tariffs_rev", UNSET)
        tariffs_rev: datetime.datetime | Unset
        if isinstance(_tariffs_rev, Unset):
            tariffs_rev = UNSET
        else:
            tariffs_rev = datetime.datetime.fromisoformat(_tariffs_rev)

        api_meta = cls(
            generated_at=generated_at,
            sources=sources,
            attribution=attribution,
            provisional=provisional,
            tariffs_rev=tariffs_rev,
        )

        api_meta.additional_properties = d
        return api_meta

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
