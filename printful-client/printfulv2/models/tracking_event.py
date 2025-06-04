import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrackingEvent")


@_attrs_define
class TrackingEvent:
    """
    Attributes:
        triggered_at (Union[Unset, datetime.datetime]):  Example: 2023-06-15T19:15:05Z.
        description (Union[Unset, str]):  Example: Arrived At Destination.
    """

    triggered_at: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        triggered_at: Union[Unset, str] = UNSET
        if not isinstance(self.triggered_at, Unset):
            triggered_at = self.triggered_at.isoformat()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if triggered_at is not UNSET:
            field_dict["triggered_at"] = triggered_at
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _triggered_at = d.pop("triggered_at", UNSET)
        triggered_at: Union[Unset, datetime.datetime]
        if isinstance(_triggered_at, Unset):
            triggered_at = UNSET
        else:
            triggered_at = isoparse(_triggered_at)

        description = d.pop("description", UNSET)

        tracking_event = cls(
            triggered_at=triggered_at,
            description=description,
        )

        tracking_event.additional_properties = d
        return tracking_event

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
