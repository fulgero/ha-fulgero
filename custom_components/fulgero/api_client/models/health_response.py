from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sources import Sources


T = TypeVar("T", bound="HealthResponse")


@_attrs_define
class HealthResponse:
    """
    Attributes:
        status (str):
        generated_at (datetime.datetime):
        sources (Sources):
        attribution (str):
    """

    status: str
    generated_at: datetime.datetime
    sources: Sources
    attribution: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        generated_at = self.generated_at.isoformat()

        sources = self.sources.to_dict()

        attribution = self.attribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "generated_at": generated_at,
                "sources": sources,
                "attribution": attribution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sources import Sources

        d = dict(src_dict)
        status = d.pop("status")

        generated_at = datetime.datetime.fromisoformat(d.pop("generated_at"))

        sources = Sources.from_dict(d.pop("sources"))

        attribution = d.pop("attribution")

        health_response = cls(
            status=status,
            generated_at=generated_at,
            sources=sources,
            attribution=attribution,
        )

        health_response.additional_properties = d
        return health_response

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
