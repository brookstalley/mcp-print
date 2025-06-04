from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_warehouse_products_response_200_data_item_warehouse_variants_item_dimensions import (
        GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensions,
    )
    from ..models.get_warehouse_products_response_200_data_item_warehouse_variants_item_links import (
        GetWarehouseProductsResponse200DataItemWarehouseVariantsItemLinks,
    )


T = TypeVar("T", bound="GetWarehouseProductsResponse200DataItemWarehouseVariantsItem")


@_attrs_define
class GetWarehouseProductsResponse200DataItemWarehouseVariantsItem:
    """
    Attributes:
        id (int): Unique identifier of the variant Example: 32453.
        name (str): Name of the variant Example: Black Heather.
        sku (str): Stock Keeping Unit (SKU) of the variant Example: some-sku-12.
        image_url (str): URL of the variant's image Example: url.to/your/image/location.png.
        retail_price (str): Retail price of the variant Example: 32.56.
        quantity (int): Available quantity of the variant Example: 23.
        dimensions (GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensions): Dimensions of the variant
        field_links (GetWarehouseProductsResponse200DataItemWarehouseVariantsItemLinks):
    """

    id: int
    name: str
    sku: str
    image_url: str
    retail_price: str
    quantity: int
    dimensions: "GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensions"
    field_links: "GetWarehouseProductsResponse200DataItemWarehouseVariantsItemLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sku = self.sku

        image_url = self.image_url

        retail_price = self.retail_price

        quantity = self.quantity

        dimensions = self.dimensions.to_dict()

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "sku": sku,
                "image_url": image_url,
                "retail_price": retail_price,
                "quantity": quantity,
                "dimensions": dimensions,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_warehouse_products_response_200_data_item_warehouse_variants_item_dimensions import (
            GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensions,
        )
        from ..models.get_warehouse_products_response_200_data_item_warehouse_variants_item_links import (
            GetWarehouseProductsResponse200DataItemWarehouseVariantsItemLinks,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sku = d.pop("sku")

        image_url = d.pop("image_url")

        retail_price = d.pop("retail_price")

        quantity = d.pop("quantity")

        dimensions = GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensions.from_dict(
            d.pop("dimensions")
        )

        field_links = GetWarehouseProductsResponse200DataItemWarehouseVariantsItemLinks.from_dict(d.pop("_links"))

        get_warehouse_products_response_200_data_item_warehouse_variants_item = cls(
            id=id,
            name=name,
            sku=sku,
            image_url=image_url,
            retail_price=retail_price,
            quantity=quantity,
            dimensions=dimensions,
            field_links=field_links,
        )

        get_warehouse_products_response_200_data_item_warehouse_variants_item.additional_properties = d
        return get_warehouse_products_response_200_data_item_warehouse_variants_item

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
