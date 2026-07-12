from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.formula_info_formula import FormulaInfoFormula


T = TypeVar("T", bound="FormulaInfo")


@_attrs_define
class FormulaInfo:
    """
    Attributes:
        offer_id (str):
        offer_name (str):
        formula (FormulaInfoFormula):
        built_in (bool):
    """

    offer_id: str
    offer_name: str
    formula: FormulaInfoFormula
    built_in: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offer_id = self.offer_id

        offer_name = self.offer_name

        formula = self.formula.to_dict()

        built_in = self.built_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offer_id": offer_id,
                "offer_name": offer_name,
                "formula": formula,
                "built_in": built_in,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.formula_info_formula import FormulaInfoFormula

        d = dict(src_dict)
        offer_id = d.pop("offer_id")

        offer_name = d.pop("offer_name")

        formula = FormulaInfoFormula.from_dict(d.pop("formula"))

        built_in = d.pop("built_in")

        formula_info = cls(
            offer_id=offer_id,
            offer_name=offer_name,
            formula=formula,
            built_in=built_in,
        )

        formula_info.additional_properties = d
        return formula_info

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
