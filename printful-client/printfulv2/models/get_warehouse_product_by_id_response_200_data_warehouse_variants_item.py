from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item_dimensions import (
        GetWarehouseProductByIdResponse200DataWarehouseVariantsItemDimensions,
    )
    from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item_links import (
        GetWarehouseProductByIdResponse200DataWarehouseVariantsItemLinks,
    )
    from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item_stock_location_item import (
        GetWarehouseProductByIdResponse200DataWarehouseVariantsItemStockLocationItem,
    )


T = TypeVar("T", bound="GetWarehouseProductByIdResponse200DataWarehouseVariantsItem")


@_attrs_define
class GetWarehouseProductByIdResponse200DataWarehouseVariantsItem:
    """
    Attributes:
        id (int): Unique identifier of the warehouse variant Example: 32453.
        name (str): Name of the variant Example: Black Heather.
        sku (str): Stock Keeping Unit (SKU) of the warehouse variant Example: some-sku-12.
        image_url (str): URL of the variant's image Example: url.to/your/image/location.png.
        retail_price (str): Retail price of the variant Example: 32.56.
        quantity (int): Available quantity of the variant Example: 23.
        stock_location (list['GetWarehouseProductByIdResponse200DataWarehouseVariantsItemStockLocationItem']): Stock
            location of the variant
        dimensions (GetWarehouseProductByIdResponse200DataWarehouseVariantsItemDimensions): Dimensions of the variant
        field_links (GetWarehouseProductByIdResponse200DataWarehouseVariantsItemLinks):
    """

    id: int
    name: str
    sku: str
    image_url: str
    retail_price: str
    quantity: int
    stock_location: list["GetWarehouseProductByIdResponse200DataWarehouseVariantsItemStockLocationItem"]
    dimensions: "GetWarehouseProductByIdResponse200DataWarehouseVariantsItemDimensions"
    field_links: "GetWarehouseProductByIdResponse200DataWarehouseVariantsItemLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        sku = self.sku

        image_url = self.image_url

        retail_price = self.retail_price

        quantity = self.quantity

        stock_location = []
        for stock_location_item_data in self.stock_location:
            stock_location_item = stock_location_item_data.to_dict()
            stock_location.append(stock_location_item)

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
                "stock_location": stock_location,
                "dimensions": dimensions,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item_dimensions import (
            GetWarehouseProductByIdResponse200DataWarehouseVariantsItemDimensions,
        )
        from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item_links import (
            GetWarehouseProductByIdResponse200DataWarehouseVariantsItemLinks,
        )
        from ..models.get_warehouse_product_by_id_response_200_data_warehouse_variants_item_stock_location_item import (
            GetWarehouseProductByIdResponse200DataWarehouseVariantsItemStockLocationItem,
        )

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        sku = d.pop("sku")

        image_url = d.pop("image_url")

        retail_price = d.pop("retail_price")

        quantity = d.pop("quantity")

        stock_location = []
        _stock_location = d.pop("stock_location")
        for stock_location_item_data in _stock_location:
            stock_location_item = (
                GetWarehouseProductByIdResponse200DataWarehouseVariantsItemStockLocationItem.from_dict(
                    stock_location_item_data
                )
            )

            stock_location.append(stock_location_item)

        dimensions = GetWarehouseProductByIdResponse200DataWarehouseVariantsItemDimensions.from_dict(
            d.pop("dimensions")
        )

        field_links = GetWarehouseProductByIdResponse200DataWarehouseVariantsItemLinks.from_dict(d.pop("_links"))

        get_warehouse_product_by_id_response_200_data_warehouse_variants_item = cls(
            id=id,
            name=name,
            sku=sku,
            image_url=image_url,
            retail_price=retail_price,
            quantity=quantity,
            stock_location=stock_location,
            dimensions=dimensions,
            field_links=field_links,
        )

        get_warehouse_product_by_id_response_200_data_warehouse_variants_item.additional_properties = d
        return get_warehouse_product_by_id_response_200_data_warehouse_variants_item

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
