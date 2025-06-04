from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeasurementValue")


@_attrs_define
class MeasurementValue:
    """The measurement value for a specific size

    Attributes:
        size (str): The size with which the value is associated Example: S.
        value (Union[Unset, str]): The single value associated with a size (whether this or `min_value` and `max_value`
            will be present) Example: 23.5.
        min_value (Union[Unset, str]): The lower boundary of the value range (whether this and `max_value` or `value`
            will be present) Example: 20.
        max_value (Union[Unset, str]): The upper boundary of the value range (whether this and `min_value` or `value`
            will be present) Example: 20.
    """

    size: str
    value: Union[Unset, str] = UNSET
    min_value: Union[Unset, str] = UNSET
    max_value: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        size = self.size

        value = self.value

        min_value = self.min_value

        max_value = self.max_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "size": size,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value
        if min_value is not UNSET:
            field_dict["min_value"] = min_value
        if max_value is not UNSET:
            field_dict["max_value"] = max_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        size = d.pop("size")

        value = d.pop("value", UNSET)

        min_value = d.pop("min_value", UNSET)

        max_value = d.pop("max_value", UNSET)

        measurement_value = cls(
            size=size,
            value=value,
            min_value=min_value,
            max_value=max_value,
        )

        measurement_value.additional_properties = d
        return measurement_value

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
