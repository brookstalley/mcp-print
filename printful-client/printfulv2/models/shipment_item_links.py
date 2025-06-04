from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_item_links_order_item import ShipmentItemLinksOrderItem


T = TypeVar("T", bound="ShipmentItemLinks")


@_attrs_define
class ShipmentItemLinks:
    """
    Attributes:
        order_item (Union[Unset, ShipmentItemLinksOrderItem]):
    """

    order_item: Union[Unset, "ShipmentItemLinksOrderItem"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order_item, Unset):
            order_item = self.order_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_item is not UNSET:
            field_dict["order_item"] = order_item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shipment_item_links_order_item import ShipmentItemLinksOrderItem

        d = dict(src_dict)
        _order_item = d.pop("order_item", UNSET)
        order_item: Union[Unset, ShipmentItemLinksOrderItem]
        if isinstance(_order_item, Unset):
            order_item = UNSET
        else:
            order_item = ShipmentItemLinksOrderItem.from_dict(_order_item)

        shipment_item_links = cls(
            order_item=order_item,
        )

        shipment_item_links.additional_properties = d
        return shipment_item_links

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
