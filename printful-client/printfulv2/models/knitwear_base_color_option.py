from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knitwear_base_color_option_name import KnitwearBaseColorOptionName
from ..models.knitwear_option_value import KnitwearOptionValue

T = TypeVar("T", bound="KnitwearBaseColorOption")


@_attrs_define
class KnitwearBaseColorOption:
    """Used to specify the base color on a knitwear product.

    Attributes:
        name (KnitwearBaseColorOptionName): Option identifier Example: base_color.
        value (KnitwearOptionValue): Option value Example: #fdfafa.
    """

    name: KnitwearBaseColorOptionName
    value: KnitwearOptionValue
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        value = self.value.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = KnitwearBaseColorOptionName(d.pop("name"))

        value = KnitwearOptionValue(d.pop("value"))

        knitwear_base_color_option = cls(
            name=name,
            value=value,
        )

        knitwear_base_color_option.additional_properties = d
        return knitwear_base_color_option

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
