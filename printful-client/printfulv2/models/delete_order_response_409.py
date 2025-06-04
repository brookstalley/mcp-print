from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delete_order_response_409_error import DeleteOrderResponse409Error


T = TypeVar("T", bound="DeleteOrderResponse409")


@_attrs_define
class DeleteOrderResponse409:
    """
    Attributes:
        code (Union[Unset, int]): Response status code `409` Example: 409.
        result (Union[Unset, str]): An error message describing a conflict between the request and the current state of
            the resource. Example: Attempting to update a resource that is already being updated. Please try again after the
            previous update has completed.
        error (Union[Unset, DeleteOrderResponse409Error]):
    """

    code: Union[Unset, int] = UNSET
    result: Union[Unset, str] = UNSET
    error: Union[Unset, "DeleteOrderResponse409Error"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        result = self.result

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_order_response_409_error import DeleteOrderResponse409Error

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        result = d.pop("result", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, DeleteOrderResponse409Error]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = DeleteOrderResponse409Error.from_dict(_error)

        delete_order_response_409 = cls(
            code=code,
            result=result,
            error=error,
        )

        delete_order_response_409.additional_properties = d
        return delete_order_response_409

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
