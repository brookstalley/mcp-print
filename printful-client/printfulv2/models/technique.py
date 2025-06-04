from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Technique")


@_attrs_define
class Technique:
    """Information about the available Product's technique

    Attributes:
        key (str): Technique key Example: embroidery.
        display_name (str): Technique display name Example: Embroidery.
        is_default (bool): This is the default product technique Example: True.
    """

    key: str
    display_name: str
    is_default: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        display_name = self.display_name

        is_default = self.is_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "display_name": display_name,
                "is_default": is_default,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        display_name = d.pop("display_name")

        is_default = d.pop("is_default")

        technique = cls(
            key=key,
            display_name=display_name,
            is_default=is_default,
        )

        technique.additional_properties = d
        return technique

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
