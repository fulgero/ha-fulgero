from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_meta import ApiMeta
    from ..models.formula_info import FormulaInfo


T = TypeVar("T", bound="FormulasResponse")


@_attrs_define
class FormulasResponse:
    """
    Attributes:
        meta (ApiMeta):
        formulas (list[FormulaInfo] | Unset):
    """

    meta: ApiMeta
    formulas: list[FormulaInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta = self.meta.to_dict()

        formulas: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.formulas, Unset):
            formulas = []
            for formulas_item_data in self.formulas:
                formulas_item = formulas_item_data.to_dict()
                formulas.append(formulas_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
            }
        )
        if formulas is not UNSET:
            field_dict["formulas"] = formulas

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_meta import ApiMeta
        from ..models.formula_info import FormulaInfo

        d = dict(src_dict)
        meta = ApiMeta.from_dict(d.pop("meta"))

        _formulas = d.pop("formulas", UNSET)
        formulas: list[FormulaInfo] | Unset = UNSET
        if _formulas is not UNSET:
            formulas = []
            for formulas_item_data in _formulas:
                formulas_item = FormulaInfo.from_dict(formulas_item_data)

                formulas.append(formulas_item)

        formulas_response = cls(
            meta=meta,
            formulas=formulas,
        )

        formulas_response.additional_properties = d
        return formulas_response

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
