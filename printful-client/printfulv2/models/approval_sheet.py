from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.approval_sheet_status import ApprovalSheetStatus

if TYPE_CHECKING:
    from ..models.approval_sheet_approval_sheet_links import ApprovalSheetApprovalSheetLinks


T = TypeVar("T", bound="ApprovalSheet")


@_attrs_define
class ApprovalSheet:
    """Approval sheet

    Attributes:
        confirm_hash (str): Confirmation hash value. Example: a14e51714be01f98487fcf5131727d31.
        status (ApprovalSheetStatus): Status of Approval Sheet. Example: waiting_for_action.
        submitted_design (str): URL to submitted design. Example: https://s3.staging.printful.com/upload/approval-
            design/ae/ae7b3d3e965c238b3e5c1a4e15696f07_l.
        recommended_design (str): URL to recommended design. Example: https://s3.staging.printful.com/upload/approval-
            design/aa/aaf9e1c6b32cb7a2c04d2746108d4124_l.
        approval_sheet (str): URL to Approval sheet. Example: ​https://example.com/approval-sheet.pdf.
        order_id (int): Order ID. Example: 123.
        order_item_id (int): Item ID. Example: 123.
        field_links (ApprovalSheetApprovalSheetLinks): HATEOAS links
    """

    confirm_hash: str
    status: ApprovalSheetStatus
    submitted_design: str
    recommended_design: str
    approval_sheet: str
    order_id: int
    order_item_id: int
    field_links: "ApprovalSheetApprovalSheetLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirm_hash = self.confirm_hash

        status = self.status.value

        submitted_design = self.submitted_design

        recommended_design = self.recommended_design

        approval_sheet = self.approval_sheet

        order_id = self.order_id

        order_item_id = self.order_item_id

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "confirm_hash": confirm_hash,
                "status": status,
                "submitted_design": submitted_design,
                "recommended_design": recommended_design,
                "approval_sheet": approval_sheet,
                "order_id": order_id,
                "order_item_id": order_item_id,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approval_sheet_approval_sheet_links import ApprovalSheetApprovalSheetLinks

        d = dict(src_dict)
        confirm_hash = d.pop("confirm_hash")

        status = ApprovalSheetStatus(d.pop("status"))

        submitted_design = d.pop("submitted_design")

        recommended_design = d.pop("recommended_design")

        approval_sheet = d.pop("approval_sheet")

        order_id = d.pop("order_id")

        order_item_id = d.pop("order_item_id")

        field_links = ApprovalSheetApprovalSheetLinks.from_dict(d.pop("_links"))

        approval_sheet = cls(
            confirm_hash=confirm_hash,
            status=status,
            submitted_design=submitted_design,
            recommended_design=recommended_design,
            approval_sheet=approval_sheet,
            order_id=order_id,
            order_item_id=order_item_id,
            field_links=field_links,
        )

        approval_sheet.additional_properties = d
        return approval_sheet

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
