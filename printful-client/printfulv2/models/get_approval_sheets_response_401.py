from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_approval_sheets_response_401_error import GetApprovalSheetsResponse401Error


T = TypeVar("T", bound="GetApprovalSheetsResponse401")


@_attrs_define
class GetApprovalSheetsResponse401:
    """
    Attributes:
        data (Union[Unset, str]): Actual error message Example: Malformed Authorization header.
        error (Union[Unset, GetApprovalSheetsResponse401Error]):
    """

    data: Union[Unset, str] = UNSET
    error: Union[Unset, "GetApprovalSheetsResponse401Error"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_approval_sheets_response_401_error import GetApprovalSheetsResponse401Error

        d = dict(src_dict)
        data = d.pop("data", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, GetApprovalSheetsResponse401Error]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = GetApprovalSheetsResponse401Error.from_dict(_error)

        get_approval_sheets_response_401 = cls(
            data=data,
            error=error,
        )

        get_approval_sheets_response_401.additional_properties = d
        return get_approval_sheets_response_401

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
