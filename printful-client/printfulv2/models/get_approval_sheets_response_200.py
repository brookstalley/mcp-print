from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.approval_sheet import ApprovalSheet
    from ..models.get_approval_sheets_response_200_approval_sheet_links import (
        GetApprovalSheetsResponse200ApprovalSheetLinks,
    )


T = TypeVar("T", bound="GetApprovalSheetsResponse200")


@_attrs_define
class GetApprovalSheetsResponse200:
    """
    Attributes:
        data (list['ApprovalSheet']):
        field_links (GetApprovalSheetsResponse200ApprovalSheetLinks): HATEOAS links
    """

    data: list["ApprovalSheet"]
    field_links: "GetApprovalSheetsResponse200ApprovalSheetLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

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
        from ..models.approval_sheet import ApprovalSheet
        from ..models.get_approval_sheets_response_200_approval_sheet_links import (
            GetApprovalSheetsResponse200ApprovalSheetLinks,
        )

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = ApprovalSheet.from_dict(data_item_data)

            data.append(data_item)

        field_links = GetApprovalSheetsResponse200ApprovalSheetLinks.from_dict(d.pop("_links"))

        get_approval_sheets_response_200 = cls(
            data=data,
            field_links=field_links,
        )

        get_approval_sheets_response_200.additional_properties = d
        return get_approval_sheets_response_200

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
