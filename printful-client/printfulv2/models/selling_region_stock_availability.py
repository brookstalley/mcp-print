from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.selling_region_stock_availability_availability import SellingRegionStockAvailabilityAvailability
from ..models.selling_region_stock_availability_name import SellingRegionStockAvailabilityName

if TYPE_CHECKING:
    from ..models.selling_region_stock_availability_placement_option_availability_item import (
        SellingRegionStockAvailabilityPlacementOptionAvailabilityItem,
    )


T = TypeVar("T", bound="SellingRegionStockAvailability")


@_attrs_define
class SellingRegionStockAvailability:
    """
    Attributes:
        name (SellingRegionStockAvailabilityName): Name of the selling region for which the stock availability apply
        availability (SellingRegionStockAvailabilityAvailability): Availability status:
              * in stock: The product is stocked in this region and fulfillable with the specified technique
              * out of stock: Product went out of stock at the supplier in this region but is fulfillable with the specified
            technique
              * not fulfillable: (a) Printful does not stock this product in this region; or (b) the product is not
            fulfillable with the specified technique in this region
              * unknown: The exact stock status could not be determined
        placement_option_availability (list['SellingRegionStockAvailabilityPlacementOptionAvailabilityItem']):
            Availability of a placement options for a catalog variant in a specified selling region. If a placement option
            is present in this array and availability is set to true it means it is available for this product. If it is set
            to false it means that the placement option is available for the variant, but not currently fulfillable for the
            given selling region settings. If an option is not present in the array but is present as an option on the
            product (see: [Retrieve a single catalog product](#tag/Catalog-v2/operation/getProducts)) it means the option is
            always available for that product.
    """

    name: SellingRegionStockAvailabilityName
    availability: SellingRegionStockAvailabilityAvailability
    placement_option_availability: list["SellingRegionStockAvailabilityPlacementOptionAvailabilityItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        availability = self.availability.value

        placement_option_availability = []
        for placement_option_availability_item_data in self.placement_option_availability:
            placement_option_availability_item = placement_option_availability_item_data.to_dict()
            placement_option_availability.append(placement_option_availability_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "availability": availability,
                "placement_option_availability": placement_option_availability,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.selling_region_stock_availability_placement_option_availability_item import (
            SellingRegionStockAvailabilityPlacementOptionAvailabilityItem,
        )

        d = dict(src_dict)
        name = SellingRegionStockAvailabilityName(d.pop("name"))

        availability = SellingRegionStockAvailabilityAvailability(d.pop("availability"))

        placement_option_availability = []
        _placement_option_availability = d.pop("placement_option_availability")
        for placement_option_availability_item_data in _placement_option_availability:
            placement_option_availability_item = (
                SellingRegionStockAvailabilityPlacementOptionAvailabilityItem.from_dict(
                    placement_option_availability_item_data
                )
            )

            placement_option_availability.append(placement_option_availability_item)

        selling_region_stock_availability = cls(
            name=name,
            availability=availability,
            placement_option_availability=placement_option_availability,
        )

        selling_region_stock_availability.additional_properties = d
        return selling_region_stock_availability

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
