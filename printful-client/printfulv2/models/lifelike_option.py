from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lifelike_option_name import LifelikeOptionName

T = TypeVar("T", bound="LifelikeOption")


@_attrs_define
class LifelikeOption:
    """Specifies if generated mockup should use lifelike effect

    Attributes:
        name (LifelikeOptionName): Option identifier Example: lifelike.
        value (bool): Whether generated mockup should use lifelike effect. Example: True.
    """

    name: LifelikeOptionName
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
        name = LifelikeOptionName(d.pop("name"))

        value = d.pop("value")

        lifelike_option = cls(
            name=name,
            value=value,
        )

        lifelike_option.additional_properties = d
        return lifelike_option

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
