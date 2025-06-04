from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_warehouse_product_by_id_response_200_data_status import GetWarehouseProductByIdResponse200DataStatus

if TYPE_CHECKING:
    from ..models.get_warehouse_product_by_id_response_200_data_links import GetWarehouseProductByIdResponse200DataLinks
    from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item import (
        GetWarehouseProductByIdResponse200DataWarehouseVariantsItem,
    )


T = TypeVar("T", bound="GetWarehouseProductByIdResponse200Data")


@_attrs_define
class GetWarehouseProductByIdResponse200Data:
    """
    Attributes:
        id (int): Unique identifier of the warehouse product Example: 356.
        name (str): Name of the warehouse product Example: Black Heather.
        status (GetWarehouseProductByIdResponse200DataStatus): Current status of the warehouse product
        currency (str): Currency code for the product's pricing (e.g., "USD") Example: USD.
        image_url (str): URL of the product's image Example: https://example.com/upload/product-
            templates/d1/d1341a6efb49f59cc58172ce1c15eb20_l.
        retail_price (str): Retail price of the product (base variant) Example: 21.54.
        warehouse_variants (list['GetWarehouseProductByIdResponse200DataWarehouseVariantsItem']): Array of variant
            details for the product
        field_links (GetWarehouseProductByIdResponse200DataLinks): Links to related resources
    """

    id: int
    name: str
    status: GetWarehouseProductByIdResponse200DataStatus
    currency: str
    image_url: str
    retail_price: str
    warehouse_variants: list["GetWarehouseProductByIdResponse200DataWarehouseVariantsItem"]
    field_links: "GetWarehouseProductByIdResponse200DataLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        status = self.status.value

        currency = self.currency

        image_url = self.image_url

        retail_price = self.retail_price

        warehouse_variants = []
        for warehouse_variants_item_data in self.warehouse_variants:
            warehouse_variants_item = warehouse_variants_item_data.to_dict()
            warehouse_variants.append(warehouse_variants_item)

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "status": status,
                "currency": currency,
                "image_url": image_url,
                "retail_price": retail_price,
                "warehouse_variants": warehouse_variants,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_warehouse_product_by_id_response_200_data_links import (
            GetWarehouseProductByIdResponse200DataLinks,
        )
        from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item import (
            GetWarehouseProductByIdResponse200DataWarehouseVariantsItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        status = GetWarehouseProductByIdResponse200DataStatus(d.pop("status"))

        currency = d.pop("currency")

        image_url = d.pop("image_url")

        retail_price = d.pop("retail_price")

        warehouse_variants = []
        _warehouse_variants = d.pop("warehouse_variants")
        for warehouse_variants_item_data in _warehouse_variants:
            warehouse_variants_item = GetWarehouseProductByIdResponse200DataWarehouseVariantsItem.from_dict(
                warehouse_variants_item_data
            )

            warehouse_variants.append(warehouse_variants_item)

        field_links = GetWarehouseProductByIdResponse200DataLinks.from_dict(d.pop("_links"))

        get_warehouse_product_by_id_response_200_data = cls(
            id=id,
            name=name,
            status=status,
            currency=currency,
            image_url=image_url,
            retail_price=retail_price,
            warehouse_variants=warehouse_variants,
            field_links=field_links,
        )

        get_warehouse_product_by_id_response_200_data.additional_properties = d
        return get_warehouse_product_by_id_response_200_data

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
