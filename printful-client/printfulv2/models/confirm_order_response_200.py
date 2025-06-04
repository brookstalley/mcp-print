from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.confirm_order_response_200_links import ConfirmOrderResponse200Links
    from ..models.order import Order


T = TypeVar("T", bound="ConfirmOrderResponse200")


@_attrs_define
class ConfirmOrderResponse200:
    """
    Attributes:
        data (Order): Order
        field_links (ConfirmOrderResponse200Links): HATEOAS links
    """

    data: "Order"
    field_links: "ConfirmOrderResponse200Links"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirm_order_response_200_links import ConfirmOrderResponse200Links
        from ..models.order import Order

        d = dict(src_dict)
        data = Order.from_dict(d.pop("data"))

        field_links = ConfirmOrderResponse200Links.from_dict(d.pop("_links"))

        confirm_order_response_200 = cls(
            data=data,
            field_links=field_links,
        )

        confirm_order_response_200.additional_properties = d
        return confirm_order_response_200

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
