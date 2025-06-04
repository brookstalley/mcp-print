from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inside_label_type_option_name import InsideLabelTypeOptionName
from ..models.inside_label_type_option_value import InsideLabelTypeOptionValue

T = TypeVar("T", bound="InsideLabelTypeOption")


@_attrs_define
class InsideLabelTypeOption:
    """Specify the type of inside label

    Attributes:
        name (InsideLabelTypeOptionName): Option identifier Example: inside_label_type.
        value (InsideLabelTypeOptionValue): Specifies type of inside label design that should be used
    """

    name: InsideLabelTypeOptionName
    value: InsideLabelTypeOptionValue
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
        name = InsideLabelTypeOptionName(d.pop("name"))

        value = InsideLabelTypeOptionValue(d.pop("value"))

        inside_label_type_option = cls(
            name=name,
            value=value,
        )

        inside_label_type_option.additional_properties = d
        return inside_label_type_option

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
