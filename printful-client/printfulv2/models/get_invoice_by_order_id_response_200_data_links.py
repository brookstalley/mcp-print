from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_invoice_by_order_id_response_200_data_links_order import (
        GetInvoiceByOrderIdResponse200DataLinksOrder,
    )
    from ..models.get_invoice_by_order_id_response_200_data_links_self import (
        GetInvoiceByOrderIdResponse200DataLinksSelf,
    )


T = TypeVar("T", bound="GetInvoiceByOrderIdResponse200DataLinks")


@_attrs_define
class GetInvoiceByOrderIdResponse200DataLinks:
    """HATEOAS links

    Attributes:
        self_ (GetInvoiceByOrderIdResponse200DataLinksSelf):
        order (GetInvoiceByOrderIdResponse200DataLinksOrder):
    """

    self_: "GetInvoiceByOrderIdResponse200DataLinksSelf"
    order: "GetInvoiceByOrderIdResponse200DataLinksOrder"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        order = self.order.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "order": order,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_invoice_by_order_id_response_200_data_links_order import (
            GetInvoiceByOrderIdResponse200DataLinksOrder,
        )
        from ..models.get_invoice_by_order_id_response_200_data_links_self import (
            GetInvoiceByOrderIdResponse200DataLinksSelf,
        )

        d = dict(src_dict)
        self_ = GetInvoiceByOrderIdResponse200DataLinksSelf.from_dict(d.pop("self"))

        order = GetInvoiceByOrderIdResponse200DataLinksOrder.from_dict(d.pop("order"))

        get_invoice_by_order_id_response_200_data_links = cls(
            self_=self_,
            order=order,
        )

        get_invoice_by_order_id_response_200_data_links.additional_properties = d
        return get_invoice_by_order_id_response_200_data_links

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
