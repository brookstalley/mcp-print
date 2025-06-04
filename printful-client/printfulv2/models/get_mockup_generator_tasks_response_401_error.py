from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetMockupGeneratorTasksResponse401Error")


@_attrs_define
class GetMockupGeneratorTasksResponse401Error:
    """
    Attributes:
        reason (Union[Unset, str]):  Example: BadRequest.
        message (Union[Unset, str]):  Example: Malformed Authorization header..
    """

    reason: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reason = self.reason

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reason = d.pop("reason", UNSET)

        message = d.pop("message", UNSET)

        get_mockup_generator_tasks_response_401_error = cls(
            reason=reason,
            message=message,
        )

        get_mockup_generator_tasks_response_401_error.additional_properties = d
        return get_mockup_generator_tasks_response_401_error

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
