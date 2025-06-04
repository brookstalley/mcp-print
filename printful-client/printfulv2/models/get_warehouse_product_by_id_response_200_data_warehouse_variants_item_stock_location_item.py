from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetWarehouseProductByIdResponse200DataWarehouseVariantsItemStockLocationItem")


@_attrs_define
class GetWarehouseProductByIdResponse200DataWarehouseVariantsItemStockLocationItem:
    """
    Attributes:
        facility (str): Name of the warehouse facility Example: Charlotte Steele Point, United States.
        stocked (int): Total quantity of product variant in our stock Example: 10.
        available (int): Available quantity of product variant in our stock Example: 10.
    """

    facility: str
    stocked: int
    available: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        facility = self.facility

        stocked = self.stocked

        available = self.available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "facility": facility,
                "stocked": stocked,
                "available": available,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        facility = d.pop("facility")

        stocked = d.pop("stocked")

        available = d.pop("available")

        get_warehouse_product_by_id_response_200_data_warehouse_variants_item_stock_location_item = cls(
            facility=facility,
            stocked=stocked,
            available=available,
        )

        get_warehouse_product_by_id_response_200_data_warehouse_variants_item_stock_location_item.additional_properties = d
        return get_warehouse_product_by_id_response_200_data_warehouse_variants_item_stock_location_item

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
