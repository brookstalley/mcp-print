from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.measurement_value import MeasurementValue


T = TypeVar("T", bound="Measurement")


@_attrs_define
class Measurement:
    """The information about a single size table measurement

    Attributes:
        type_label (str): Measurement type Example: Length.
        unit (str): The measurement unit if it's not defined on the size table level or is different Example: none.
        values (list['MeasurementValue']): The measurement values for each size
    """

    type_label: str
    unit: str
    values: list["MeasurementValue"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_label = self.type_label

        unit = self.unit

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type_label": type_label,
                "unit": unit,
                "values": values,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement_value import MeasurementValue

        d = dict(src_dict)
        type_label = d.pop("type_label")

        unit = d.pop("unit")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = MeasurementValue.from_dict(values_item_data)

            values.append(values_item)

        measurement = cls(
            type_label=type_label,
            unit=unit,
            values=values,
        )

        measurement.additional_properties = d
        return measurement

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
