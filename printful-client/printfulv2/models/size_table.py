from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.size_table_type import SizeTableType
from ..models.size_table_unit import SizeTableUnit

if TYPE_CHECKING:
    from ..models.measurement import Measurement


T = TypeVar("T", bound="SizeTable")


@_attrs_define
class SizeTable:
    """Size table for the Product

    Attributes:
        type_ (SizeTableType): Size table type
        unit (SizeTableUnit): The unit the size table values are in
        description (str): The size table description (HTML)
        image_url (str): The URL of an image showing the measurements
        image_description (str): The description of the measurement image (HTML)
        measurements (list['Measurement']): The size table measurements
    """

    type_: SizeTableType
    unit: SizeTableUnit
    description: str
    image_url: str
    image_description: str
    measurements: list["Measurement"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        unit = self.unit.value

        description = self.description

        image_url = self.image_url

        image_description = self.image_description

        measurements = []
        for measurements_item_data in self.measurements:
            measurements_item = measurements_item_data.to_dict()
            measurements.append(measurements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "unit": unit,
                "description": description,
                "image_url": image_url,
                "image_description": image_description,
                "measurements": measurements,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.measurement import Measurement

        d = dict(src_dict)
        type_ = SizeTableType(d.pop("type"))

        unit = SizeTableUnit(d.pop("unit"))

        description = d.pop("description")

        image_url = d.pop("image_url")

        image_description = d.pop("image_description")

        measurements = []
        _measurements = d.pop("measurements")
        for measurements_item_data in _measurements:
            measurements_item = Measurement.from_dict(measurements_item_data)

            measurements.append(measurements_item)

        size_table = cls(
            type_=type_,
            unit=unit,
            description=description,
            image_url=image_url,
            image_description=image_description,
            measurements=measurements,
        )

        size_table.additional_properties = d
        return size_table

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
