from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CostsByVariantItem")


@_attrs_define
class CostsByVariantItem:
    """
    Attributes:
        variant_id (int): Variant ID. See [Catalog API](#tag/Catalog-API).
        variant_name (str): Variant name.
        product_id (int): Product ID. See [Catalog API](#tag/Catalog-API).
        fulfillment (str): All fulfillment costs that are charged by Printful, excluding shipping.
        sales (str): Order retail price data. Available only if retail price fields are properly set up on the
            integration's side.
        quantity (int): Total quantity of items ordered from this product in the selected period.
    """

    variant_id: int
    variant_name: str
    product_id: int
    fulfillment: str
    sales: str
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variant_id = self.variant_id

        variant_name = self.variant_name

        product_id = self.product_id

        fulfillment = self.fulfillment

        sales = self.sales

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variant_id": variant_id,
                "variant_name": variant_name,
                "product_id": product_id,
                "fulfillment": fulfillment,
                "sales": sales,
                "quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        variant_id = d.pop("variant_id")

        variant_name = d.pop("variant_name")

        product_id = d.pop("product_id")

        fulfillment = d.pop("fulfillment")

        sales = d.pop("sales")

        quantity = d.pop("quantity")

        costs_by_variant_item = cls(
            variant_id=variant_id,
            variant_name=variant_name,
            product_id=product_id,
            fulfillment=fulfillment,
            sales=sales,
            quantity=quantity,
        )

        costs_by_variant_item.additional_properties = d
        return costs_by_variant_item

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
