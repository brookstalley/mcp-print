import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="WebhookShipmentData")


@_attrs_define
class WebhookShipmentData:
    """
    Attributes:
        id (int): Shipment's ID
        status (str): Shipment's status
        store_id (int): ID of the store associated with the shipment
        tracking_number (str): The tracking code associated with the shipment
        tracking_url (str): Shipment tracking URL Example: ​https://www.fedex.com/fedextrack/?tracknumbers=0000000000.
        created_at (datetime.datetime): Shipment creation date-time Example: 2023-04-05T06:07:08Z.
        ship_date (str): Ship date (`Y-m-d`) Example: 2023-03-21.
        shipped_at (datetime.datetime): Date-time of when the shipment was sent Example: 2023-04-05T06:07:08Z.
        reshipment (bool): Whether this is a reshipment
    """

    id: int
    status: str
    store_id: int
    tracking_number: str
    tracking_url: str
    created_at: datetime.datetime
    ship_date: str
    shipped_at: datetime.datetime
    reshipment: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        store_id = self.store_id

        tracking_number = self.tracking_number

        tracking_url = self.tracking_url

        created_at = self.created_at.isoformat()

        ship_date = self.ship_date

        shipped_at = self.shipped_at.isoformat()

        reshipment = self.reshipment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "store_id": store_id,
                "tracking_number": tracking_number,
                "tracking_url": tracking_url,
                "created_at": created_at,
                "ship_date": ship_date,
                "shipped_at": shipped_at,
                "reshipment": reshipment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        status = d.pop("status")

        store_id = d.pop("store_id")

        tracking_number = d.pop("tracking_number")

        tracking_url = d.pop("tracking_url")

        created_at = isoparse(d.pop("created_at"))

        ship_date = d.pop("ship_date")

        shipped_at = isoparse(d.pop("shipped_at"))

        reshipment = d.pop("reshipment")

        webhook_shipment_data = cls(
            id=id,
            status=status,
            store_id=store_id,
            tracking_number=tracking_number,
            tracking_url=tracking_url,
            created_at=created_at,
            ship_date=ship_date,
            shipped_at=shipped_at,
            reshipment=reshipment,
        )

        webhook_shipment_data.additional_properties = d
        return webhook_shipment_data

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
