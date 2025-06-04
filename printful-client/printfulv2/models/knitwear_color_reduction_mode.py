from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.knitwear_color_reduction_mode_name import KnitwearColorReductionModeName
from ..models.knitwear_color_reduction_mode_value import KnitwearColorReductionModeValue

T = TypeVar("T", bound="KnitwearColorReductionMode")


@_attrs_define
class KnitwearColorReductionMode:
    """Used to set the color reduction mode for a knitwear product

    Attributes:
        name (KnitwearColorReductionModeName): Option identifier Example: color_reduction_mode.
        value (KnitwearColorReductionModeValue): Option value Example: pixelated.
    """

    name: KnitwearColorReductionModeName
    value: KnitwearColorReductionModeValue
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
        name = KnitwearColorReductionModeName(d.pop("name"))

        value = KnitwearColorReductionModeValue(d.pop("value"))

        knitwear_color_reduction_mode = cls(
            name=name,
            value=value,
        )

        knitwear_color_reduction_mode.additional_properties = d
        return knitwear_color_reduction_mode

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
