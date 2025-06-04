from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_warehouse_products_response_200_data_item_warehouse_variants_item_dimensions_measurement_system import (
    GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensionsMeasurementSystem,
)

T = TypeVar("T", bound="GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensions")


@_attrs_define
class GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensions:
    """Dimensions of the variant

    Attributes:
        measurement_system (GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensionsMeasurementSystem):
            The system of measurement used for the dimensions.
        width (float): Width of the variant. Example: 3.21.
        height (float): Height of the variant. Example: 4.56.
        length (float): Length of the variant. (NEW) Example: 6.53.
        weight (float): Weight of the variant. Example: 3.
    """

    measurement_system: GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensionsMeasurementSystem
    width: float
    height: float
    length: float
    weight: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        measurement_system = self.measurement_system.value

        width = self.width

        height = self.height

        length = self.length

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "measurement_system": measurement_system,
                "width": width,
                "height": height,
                "length": length,
                "weight": weight,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        measurement_system = GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensionsMeasurementSystem(
            d.pop("measurement_system")
        )

        width = d.pop("width")

        height = d.pop("height")

        length = d.pop("length")

        weight = d.pop("weight")

        get_warehouse_products_response_200_data_item_warehouse_variants_item_dimensions = cls(
            measurement_system=measurement_system,
            width=width,
            height=height,
            length=length,
            weight=weight,
        )

        get_warehouse_products_response_200_data_item_warehouse_variants_item_dimensions.additional_properties = d
        return get_warehouse_products_response_200_data_item_warehouse_variants_item_dimensions

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
