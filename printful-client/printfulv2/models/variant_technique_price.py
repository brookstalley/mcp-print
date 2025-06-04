from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VariantTechniquePrice")


@_attrs_define
class VariantTechniquePrice:
    """Product prices information

    Attributes:
        technique_key (str): Key associated to the technique Example: digital.
        technique_display_name (str): Full technique name Example: Digital printing.
        price (str): Price converted to the region currency Example: 9.50.
        discounted_price (str): Discounted price per region Example: 8.50.
    """

    technique_key: str
    technique_display_name: str
    price: str
    discounted_price: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        technique_key = self.technique_key

        technique_display_name = self.technique_display_name

        price = self.price

        discounted_price = self.discounted_price

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "technique_key": technique_key,
                "technique_display_name": technique_display_name,
                "price": price,
                "discounted_price": discounted_price,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        technique_key = d.pop("technique_key")

        technique_display_name = d.pop("technique_display_name")

        price = d.pop("price")

        discounted_price = d.pop("discounted_price")

        variant_technique_price = cls(
            technique_key=technique_key,
            technique_display_name=technique_display_name,
            price=price,
            discounted_price=discounted_price,
        )

        variant_technique_price.additional_properties = d
        return variant_technique_price

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
