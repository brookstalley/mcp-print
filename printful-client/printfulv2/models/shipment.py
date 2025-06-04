import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.shipment_delivery_status import ShipmentDeliveryStatus
from ..models.shipment_shipment_status import ShipmentShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.shipment_departure_address import ShipmentDepartureAddress
    from ..models.shipment_estimated_delivery_type_0 import ShipmentEstimatedDeliveryType0
    from ..models.shipment_item import ShipmentItem
    from ..models.shipment_links import ShipmentLinks
    from ..models.tracking_event import TrackingEvent


T = TypeVar("T", bound="Shipment")


@_attrs_define
class Shipment:
    """
    Attributes:
        id (Union[Unset, int]):  Example: 1.
        order_id (Union[Unset, int]):  Example: 2.
        order_external_id (Union[None, Unset, str]):  Example: my_custom_id_1234.
        carrier (Union[None, Unset, str]): The carrier that will fulfill the shipment. Example: USPS.
        service (Union[None, Unset, str]): The service being used to fulfill the shipment. Example: USPS Priority Mail.
        shipment_status (Union[Unset, ShipmentShipmentStatus]):  Example: canceled.
        shipped_at (Union[None, Unset, datetime.datetime]):  Example: 2023-06-15T16:35:35Z.
        delivery_status (Union[Unset, ShipmentDeliveryStatus]):
        delivered_at (Union[None, Unset, datetime.datetime]):  Example: 2023-06-15T16:35:35Z.
        departure_address (Union[Unset, ShipmentDepartureAddress]):
        is_reshipment (Union[Unset, bool]): If there is an issue with items in a shipment, a reshipment might be
            necessary. This property will be false if it is the original shipment and true if it is a reshipment
        tracking_url (Union[Unset, str]):  Example: ​https://myorders.com/tracking/39925631.
        tracking_events (Union[Unset, list['TrackingEvent']]):
        estimated_delivery (Union['ShipmentEstimatedDeliveryType0', None, Unset]):
        shipment_items (Union[Unset, list['ShipmentItem']]):
        field_links (Union[Unset, ShipmentLinks]):
    """

    id: Union[Unset, int] = UNSET
    order_id: Union[Unset, int] = UNSET
    order_external_id: Union[None, Unset, str] = UNSET
    carrier: Union[None, Unset, str] = UNSET
    service: Union[None, Unset, str] = UNSET
    shipment_status: Union[Unset, ShipmentShipmentStatus] = UNSET
    shipped_at: Union[None, Unset, datetime.datetime] = UNSET
    delivery_status: Union[Unset, ShipmentDeliveryStatus] = UNSET
    delivered_at: Union[None, Unset, datetime.datetime] = UNSET
    departure_address: Union[Unset, "ShipmentDepartureAddress"] = UNSET
    is_reshipment: Union[Unset, bool] = UNSET
    tracking_url: Union[Unset, str] = UNSET
    tracking_events: Union[Unset, list["TrackingEvent"]] = UNSET
    estimated_delivery: Union["ShipmentEstimatedDeliveryType0", None, Unset] = UNSET
    shipment_items: Union[Unset, list["ShipmentItem"]] = UNSET
    field_links: Union[Unset, "ShipmentLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.shipment_estimated_delivery_type_0 import ShipmentEstimatedDeliveryType0

        id = self.id

        order_id = self.order_id

        order_external_id: Union[None, Unset, str]
        if isinstance(self.order_external_id, Unset):
            order_external_id = UNSET
        else:
            order_external_id = self.order_external_id

        carrier: Union[None, Unset, str]
        if isinstance(self.carrier, Unset):
            carrier = UNSET
        else:
            carrier = self.carrier

        service: Union[None, Unset, str]
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service

        shipment_status: Union[Unset, str] = UNSET
        if not isinstance(self.shipment_status, Unset):
            shipment_status = self.shipment_status.value

        shipped_at: Union[None, Unset, str]
        if isinstance(self.shipped_at, Unset):
            shipped_at = UNSET
        elif isinstance(self.shipped_at, datetime.datetime):
            shipped_at = self.shipped_at.isoformat()
        else:
            shipped_at = self.shipped_at

        delivery_status: Union[Unset, str] = UNSET
        if not isinstance(self.delivery_status, Unset):
            delivery_status = self.delivery_status.value

        delivered_at: Union[None, Unset, str]
        if isinstance(self.delivered_at, Unset):
            delivered_at = UNSET
        elif isinstance(self.delivered_at, datetime.datetime):
            delivered_at = self.delivered_at.isoformat()
        else:
            delivered_at = self.delivered_at

        departure_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.departure_address, Unset):
            departure_address = self.departure_address.to_dict()

        is_reshipment = self.is_reshipment

        tracking_url = self.tracking_url

        tracking_events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tracking_events, Unset):
            tracking_events = []
            for tracking_events_item_data in self.tracking_events:
                tracking_events_item = tracking_events_item_data.to_dict()
                tracking_events.append(tracking_events_item)

        estimated_delivery: Union[None, Unset, dict[str, Any]]
        if isinstance(self.estimated_delivery, Unset):
            estimated_delivery = UNSET
        elif isinstance(self.estimated_delivery, ShipmentEstimatedDeliveryType0):
            estimated_delivery = self.estimated_delivery.to_dict()
        else:
            estimated_delivery = self.estimated_delivery

        shipment_items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.shipment_items, Unset):
            shipment_items = []
            for shipment_items_item_data in self.shipment_items:
                shipment_items_item = shipment_items_item_data.to_dict()
                shipment_items.append(shipment_items_item)

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_external_id is not UNSET:
            field_dict["order_external_id"] = order_external_id
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if service is not UNSET:
            field_dict["service"] = service
        if shipment_status is not UNSET:
            field_dict["shipment_status"] = shipment_status
        if shipped_at is not UNSET:
            field_dict["shipped_at"] = shipped_at
        if delivery_status is not UNSET:
            field_dict["delivery_status"] = delivery_status
        if delivered_at is not UNSET:
            field_dict["delivered_at"] = delivered_at
        if departure_address is not UNSET:
            field_dict["departure_address"] = departure_address
        if is_reshipment is not UNSET:
            field_dict["is_reshipment"] = is_reshipment
        if tracking_url is not UNSET:
            field_dict["tracking_url"] = tracking_url
        if tracking_events is not UNSET:
            field_dict["tracking_events"] = tracking_events
        if estimated_delivery is not UNSET:
            field_dict["estimated_delivery"] = estimated_delivery
        if shipment_items is not UNSET:
            field_dict["shipment_items"] = shipment_items
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shipment_departure_address import ShipmentDepartureAddress
        from ..models.shipment_estimated_delivery_type_0 import ShipmentEstimatedDeliveryType0
        from ..models.shipment_item import ShipmentItem
        from ..models.shipment_links import ShipmentLinks
        from ..models.tracking_event import TrackingEvent

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        order_id = d.pop("order_id", UNSET)

        def _parse_order_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        order_external_id = _parse_order_external_id(d.pop("order_external_id", UNSET))

        def _parse_carrier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        carrier = _parse_carrier(d.pop("carrier", UNSET))

        def _parse_service(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        service = _parse_service(d.pop("service", UNSET))

        _shipment_status = d.pop("shipment_status", UNSET)
        shipment_status: Union[Unset, ShipmentShipmentStatus]
        if isinstance(_shipment_status, Unset):
            shipment_status = UNSET
        else:
            shipment_status = ShipmentShipmentStatus(_shipment_status)

        def _parse_shipped_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                shipped_at_type_0 = isoparse(data)

                return shipped_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        shipped_at = _parse_shipped_at(d.pop("shipped_at", UNSET))

        _delivery_status = d.pop("delivery_status", UNSET)
        delivery_status: Union[Unset, ShipmentDeliveryStatus]
        if isinstance(_delivery_status, Unset):
            delivery_status = UNSET
        else:
            delivery_status = ShipmentDeliveryStatus(_delivery_status)

        def _parse_delivered_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivered_at_type_0 = isoparse(data)

                return delivered_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        delivered_at = _parse_delivered_at(d.pop("delivered_at", UNSET))

        _departure_address = d.pop("departure_address", UNSET)
        departure_address: Union[Unset, ShipmentDepartureAddress]
        if isinstance(_departure_address, Unset):
            departure_address = UNSET
        else:
            departure_address = ShipmentDepartureAddress.from_dict(_departure_address)

        is_reshipment = d.pop("is_reshipment", UNSET)

        tracking_url = d.pop("tracking_url", UNSET)

        tracking_events = []
        _tracking_events = d.pop("tracking_events", UNSET)
        for tracking_events_item_data in _tracking_events or []:
            tracking_events_item = TrackingEvent.from_dict(tracking_events_item_data)

            tracking_events.append(tracking_events_item)

        def _parse_estimated_delivery(data: object) -> Union["ShipmentEstimatedDeliveryType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                estimated_delivery_type_0 = ShipmentEstimatedDeliveryType0.from_dict(data)

                return estimated_delivery_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ShipmentEstimatedDeliveryType0", None, Unset], data)

        estimated_delivery = _parse_estimated_delivery(d.pop("estimated_delivery", UNSET))

        shipment_items = []
        _shipment_items = d.pop("shipment_items", UNSET)
        for shipment_items_item_data in _shipment_items or []:
            shipment_items_item = ShipmentItem.from_dict(shipment_items_item_data)

            shipment_items.append(shipment_items_item)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, ShipmentLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = ShipmentLinks.from_dict(_field_links)

        shipment = cls(
            id=id,
            order_id=order_id,
            order_external_id=order_external_id,
            carrier=carrier,
            service=service,
            shipment_status=shipment_status,
            shipped_at=shipped_at,
            delivery_status=delivery_status,
            delivered_at=delivered_at,
            departure_address=departure_address,
            is_reshipment=is_reshipment,
            tracking_url=tracking_url,
            tracking_events=tracking_events,
            estimated_delivery=estimated_delivery,
            shipment_items=shipment_items,
            field_links=field_links,
        )

        shipment.additional_properties = d
        return shipment

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
