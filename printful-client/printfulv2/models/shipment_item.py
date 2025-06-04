from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_item_links import ShipmentItemLinks


T = TypeVar("T", bound="ShipmentItem")


@_attrs_define
class ShipmentItem:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 10.
        order_item_id (Union[Unset, int]):  Example: 20.
        order_item_external_id (Union[None, Unset, str]):  Example: item-external-id.
        order_item_name (Union[None, Unset, str]):  Example: Item name.
        quantity (Union[Unset, int]):  Example: 1.
        field_links (Union[Unset, ShipmentItemLinks]):
    """

    id: Union[Unset, int] = UNSET
    order_item_id: Union[Unset, int] = UNSET
    order_item_external_id: Union[None, Unset, str] = UNSET
    order_item_name: Union[None, Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    field_links: Union[Unset, "ShipmentItemLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        order_item_id = self.order_item_id

        order_item_external_id: Union[None, Unset, str]
        if isinstance(self.order_item_external_id, Unset):
            order_item_external_id = UNSET
        else:
            order_item_external_id = self.order_item_external_id

        order_item_name: Union[None, Unset, str]
        if isinstance(self.order_item_name, Unset):
            order_item_name = UNSET
        else:
            order_item_name = self.order_item_name

        quantity = self.quantity

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if order_item_id is not UNSET:
            field_dict["order_item_id"] = order_item_id
        if order_item_external_id is not UNSET:
            field_dict["order_item_external_id"] = order_item_external_id
        if order_item_name is not UNSET:
            field_dict["order_item_name"] = order_item_name
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shipment_item_links import ShipmentItemLinks

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        order_item_id = d.pop("order_item_id", UNSET)

        def _parse_order_item_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_item_external_id = _parse_order_item_external_id(d.pop("order_item_external_id", UNSET))

        def _parse_order_item_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_item_name = _parse_order_item_name(d.pop("order_item_name", UNSET))

        quantity = d.pop("quantity", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, ShipmentItemLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ShipmentItemLinks.from_dict(_field_links)

        shipment_item = cls(
            id=id,
            order_item_id=order_item_id,
            order_item_external_id=order_item_external_id,
            order_item_name=order_item_name,
            quantity=quantity,
            field_links=field_links,
        )

        shipment_item.additional_properties = d
        return shipment_item

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
