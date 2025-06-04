import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WebhookOrderData")


@_attrs_define
class WebhookOrderData:
    """
    Attributes:
        id (int): Order's ID
        external_id (str): Order's External ID
        status (str): Order's status
        store_id (int): ID of the store associated with the order
        dashboard_url (str): The URL to view the order in Printful dashboard
        created_at (datetime.datetime): Order creation date-time Example: 2023-04-05T06:07:08Z.
        updated_at (datetime.datetime): Latest order's update date-time Example: 2023-04-05T06:07:08Z.
    """

    id: int
    external_id: str
    status: str
    store_id: int
    dashboard_url: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        external_id = self.external_id

        status = self.status

        store_id = self.store_id

        dashboard_url = self.dashboard_url

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "external_id": external_id,
                "status": status,
                "store_id": store_id,
                "dashboard_url": dashboard_url,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        external_id = d.pop("external_id")

        status = d.pop("status")

        store_id = d.pop("store_id")

        dashboard_url = d.pop("dashboard_url")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        webhook_order_data = cls(
            id=id,
            external_id=external_id,
            status=status,
            store_id=store_id,
            dashboard_url=dashboard_url,
            created_at=created_at,
            updated_at=updated_at,
        )

        webhook_order_data.additional_properties = d
        return webhook_order_data

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
