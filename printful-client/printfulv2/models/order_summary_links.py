from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hateoas_link import HateoasLink


T = TypeVar("T", bound="OrderSummaryLinks")


@_attrs_define
class OrderSummaryLinks:
    """HATEOAS links

    Attributes:
        self_ (HateoasLink):
        order_items (HateoasLink):
        shipments (HateoasLink):
    """

    self_: "HateoasLink"
    order_items: "HateoasLink"
    shipments: "HateoasLink"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        order_items = self.order_items.to_dict()

        shipments = self.shipments.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "order_items": order_items,
                "shipments": shipments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hateoas_link import HateoasLink

        d = dict(src_dict)
        self_ = HateoasLink.from_dict(d.pop("self"))

        order_items = HateoasLink.from_dict(d.pop("order_items"))

        shipments = HateoasLink.from_dict(d.pop("shipments"))

        order_summary_links = cls(
            self_=self_,
            order_items=order_items,
            shipments=shipments,
        )

        order_summary_links.additional_properties = d
        return order_summary_links

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
