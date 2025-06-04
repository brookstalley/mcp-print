from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApprovalSheetWebhookFile")


@_attrs_define
class ApprovalSheetWebhookFile:
    """
    Attributes:
        confirm_hash (Union[Unset, str]):  Example: a14e51714be01f98487fcf5131727d31.
        submitted_design (Union[Unset, str]):  Example: https://s3.staging.printful.com/upload/approval-
            design/ae/ae7b3d3e965c238b3e5c1a4e15696f07_l.
        recommended_design (Union[Unset, str]):  Example: https://s3.staging.printful.com/upload/approval-
            design/aa/aaf9e1c6b32cb7a2c04d2746108d4124_l.
        approval_sheet (Union[Unset, str]):  Example: https://www.printful.test/dashboard/order/download-approval-sheet-
            pdf?confirmationHash=13aa35854bfc67a85b7ce231aef2ae8.
    """

    confirm_hash: Union[Unset, str] = UNSET
    submitted_design: Union[Unset, str] = UNSET
    recommended_design: Union[Unset, str] = UNSET
    approval_sheet: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        confirm_hash = self.confirm_hash

        submitted_design = self.submitted_design

        recommended_design = self.recommended_design

        approval_sheet = self.approval_sheet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if confirm_hash is not UNSET:
            field_dict["confirm_hash"] = confirm_hash
        if submitted_design is not UNSET:
            field_dict["submitted_design"] = submitted_design
        if recommended_design is not UNSET:
            field_dict["recommended_design"] = recommended_design
        if approval_sheet is not UNSET:
            field_dict["approval_sheet"] = approval_sheet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirm_hash = d.pop("confirm_hash", UNSET)

        submitted_design = d.pop("submitted_design", UNSET)

        recommended_design = d.pop("recommended_design", UNSET)

        approval_sheet = d.pop("approval_sheet", UNSET)

        approval_sheet_webhook_file = cls(
            confirm_hash=confirm_hash,
            submitted_design=submitted_design,
            recommended_design=recommended_design,
            approval_sheet=approval_sheet,
        )

        approval_sheet_webhook_file.additional_properties = d
        return approval_sheet_webhook_file

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
