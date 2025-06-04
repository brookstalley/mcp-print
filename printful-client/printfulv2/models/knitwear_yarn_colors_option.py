from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knitwear_option_value import KnitwearOptionValue
from ..models.knitwear_yarn_colors_option_name import KnitwearYarnColorsOptionName

T = TypeVar("T", bound="KnitwearYarnColorsOption")


@_attrs_define
class KnitwearYarnColorsOption:
    """Used to specify the yarn colors for the whole product. These are the colors that will be used across the whole
    product.

        Attributes:
            name (KnitwearYarnColorsOptionName): Option identifier Example: yarn_colors.
            value (list[KnitwearOptionValue]): Option value
    """

    name: KnitwearYarnColorsOptionName
    value: list[KnitwearOptionValue]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        value = []
        for value_item_data in self.value:
            value_item = value_item_data.value
            value.append(value_item)

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
        name = KnitwearYarnColorsOptionName(d.pop("name"))

        value = []
        _value = d.pop("value")
        for value_item_data in _value:
            value_item = KnitwearOptionValue(value_item_data)

            value.append(value_item)

        knitwear_yarn_colors_option = cls(
            name=name,
            value=value,
        )

        knitwear_yarn_colors_option.additional_properties = d
        return knitwear_yarn_colors_option

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
