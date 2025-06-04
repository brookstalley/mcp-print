from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_shipping_rate_item_source import WarehouseShippingRateItemSource

T = TypeVar("T", bound="WarehouseShippingRateItem")


@_attrs_define
class WarehouseShippingRateItem:
    """
    Attributes:
        source (WarehouseShippingRateItemSource): Warehouse source
        quantity (int): Item quantity Example: 1.
        warehouse_variant_id (int): ID of catalog variant Example: 4011.
    """

    source: WarehouseShippingRateItemSource
    quantity: int
    warehouse_variant_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source.value

        quantity = self.quantity

        warehouse_variant_id = self.warehouse_variant_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "quantity": quantity,
                "warehouse_variant_id": warehouse_variant_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = WarehouseShippingRateItemSource(d.pop("source"))

        quantity = d.pop("quantity")

        warehouse_variant_id = d.pop("warehouse_variant_id")

        warehouse_shipping_rate_item = cls(
            source=source,
            quantity=quantity,
            warehouse_variant_id=warehouse_variant_id,
        )

        warehouse_shipping_rate_item.additional_properties = d
        return warehouse_shipping_rate_item

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
