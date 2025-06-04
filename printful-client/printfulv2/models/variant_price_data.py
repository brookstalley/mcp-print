from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.variant_technique_price import VariantTechniquePrice


T = TypeVar("T", bound="VariantPriceData")


@_attrs_define
class VariantPriceData:
    """Variant with the pricing information

    Attributes:
        id (int): Variant id Example: 1.
        techniques (list['VariantTechniquePrice']): Array containing pricing information about available techniques per
            variant
    """

    id: int
    techniques: list["VariantTechniquePrice"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        techniques = []
        for techniques_item_data in self.techniques:
            techniques_item = techniques_item_data.to_dict()
            techniques.append(techniques_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "techniques": techniques,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_technique_price import VariantTechniquePrice

        d = dict(src_dict)
        id = d.pop("id")

        techniques = []
        _techniques = d.pop("techniques")
        for techniques_item_data in _techniques:
            techniques_item = VariantTechniquePrice.from_dict(techniques_item_data)

            techniques.append(techniques_item)

        variant_price_data = cls(
            id=id,
            techniques=techniques,
        )

        variant_price_data.additional_properties = d
        return variant_price_data

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
