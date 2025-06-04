from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProblemDetails")


@_attrs_define
class ProblemDetails:
    """
    Attributes:
        type_ (Union[Unset, str]): A URL that can be followed to get to our [documentation](#section/Errors) for the
            problem type.
        status (Union[Unset, int]): The HTTP status code.
        title (Union[Unset, str]): A human-readable summary of the problem type.
        details (Union[Unset, str]): A human-readable explanation specific to the occurrence of the problem.
        instance (Union[Unset, str]): Optional. A URI that uniquely identifies the specific occurence of the problem
    """

    type_: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    details: Union[Unset, str] = UNSET
    instance: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        status = self.status

        title = self.title

        details = self.details

        instance = self.instance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if details is not UNSET:
            field_dict["details"] = details
        if instance is not UNSET:
            field_dict["instance"] = instance

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        details = d.pop("details", UNSET)

        instance = d.pop("instance", UNSET)

        problem_details = cls(
            type_=type_,
            status=status,
            title=title,
            details=details,
            instance=instance,
        )

        problem_details.additional_properties = d
        return problem_details

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
