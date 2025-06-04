from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_3d_puff_option_name import Field3DPuffOptionName

T = TypeVar("T", bound="Field3DPuffOption")


@_attrs_define
class Field3DPuffOption:
    """Should thread use 3d puff technique

    Attributes:
        name (Field3DPuffOptionName): Option identifier Example: 3d_puff.
        value (bool): Whether the 3d puff technique should be used for the layer. Example: True.
    """

    name: Field3DPuffOptionName
    value: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        value = self.value

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
        name = Field3DPuffOptionName(d.pop("name"))

        value = d.pop("value")

        field_3d_puff_option = cls(
            name=name,
            value=value,
        )

        field_3d_puff_option.additional_properties = d
        return field_3d_puff_option

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
