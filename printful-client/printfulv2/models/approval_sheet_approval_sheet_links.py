from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.approval_sheet_approval_sheet_links_order import ApprovalSheetApprovalSheetLinksOrder
    from ..models.approval_sheet_approval_sheet_links_order_item import ApprovalSheetApprovalSheetLinksOrderItem


T = TypeVar("T", bound="ApprovalSheetApprovalSheetLinks")


@_attrs_define
class ApprovalSheetApprovalSheetLinks:
    """HATEOAS links

    Attributes:
        order (ApprovalSheetApprovalSheetLinksOrder):
        order_item (ApprovalSheetApprovalSheetLinksOrderItem):
    """

    order: "ApprovalSheetApprovalSheetLinksOrder"
    order_item: "ApprovalSheetApprovalSheetLinksOrderItem"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order.to_dict()

        order_item = self.order_item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "order_item": order_item,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_sheet_approval_sheet_links_order import ApprovalSheetApprovalSheetLinksOrder
        from ..models.approval_sheet_approval_sheet_links_order_item import ApprovalSheetApprovalSheetLinksOrderItem

        d = dict(src_dict)
        order = ApprovalSheetApprovalSheetLinksOrder.from_dict(d.pop("order"))

        order_item = ApprovalSheetApprovalSheetLinksOrderItem.from_dict(d.pop("order_item"))

        approval_sheet_approval_sheet_links = cls(
            order=order,
            order_item=order_item,
        )

        approval_sheet_approval_sheet_links.additional_properties = d
        return approval_sheet_approval_sheet_links

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
