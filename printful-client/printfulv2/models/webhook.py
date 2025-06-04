import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="Webhook")


@_attrs_define
class Webhook:
    """
    Attributes:
        type_ (str): Event type
        occurred_at (datetime.datetime): Event time Example: 2023-04-05T06:07:08Z.
        retries (int): Number of previous attempts to deliver this webhook event Example: 2.
        store_id (int): ID of the store that the event occurred to Example: 12.
    """

    type_: str
    occurred_at: datetime.datetime
    retries: int
    store_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        occurred_at = self.occurred_at.isoformat()

        retries = self.retries

        store_id = self.store_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "occurred_at": occurred_at,
                "retries": retries,
                "store_id": store_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        occurred_at = isoparse(d.pop("occurred_at"))

        retries = d.pop("retries")

        store_id = d.pop("store_id")

        webhook = cls(
            type_=type_,
            occurred_at=occurred_at,
            retries=retries,
            store_id=store_id,
        )

        webhook.additional_properties = d
        return webhook

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
