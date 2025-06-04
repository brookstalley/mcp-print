import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_configuration import EventConfiguration


T = TypeVar("T", bound="WebhookInfo")


@_attrs_define
class WebhookInfo:
    r"""
    Attributes:
        default_url (Union[None, str]): Webhook URL (HTTPS-only) that will receive store's event notifications if no URL
            is set for the event. Example: ​https://www.example.com/printful/webhook.
        expires_at (Union[None, datetime.datetime]): Date-time indicating when the configuration will expire. The
            default value is `null` meaning it won't expire. Example: 2023-04-05T06:07:08Z.
        events (list['EventConfiguration']): Array of enabled webhook event configurations Example: [{'type':
            'shipment_sent', 'url': '\u200bhttps://www.example.com/printful/webhook/shipment_sent'}, {'type':
            'catalog_stock_updated', 'params': [{'name': 'products', 'value': [{'id': 1}, {'id': 71}]}]}].
        public_key (Union[Unset, str]): Public key used to identify the specific settings. Example: SbF/9d/uWguI.
    """

    default_url: Union[None, str]
    expires_at: Union[None, datetime.datetime]
    events: list["EventConfiguration"]
    public_key: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_url: Union[None, str]
        default_url = self.default_url

        expires_at: Union[None, str]
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        public_key = self.public_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "default_url": default_url,
                "expires_at": expires_at,
                "events": events,
            }
        )
        if public_key is not UNSET:
            field_dict["public_key"] = public_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_configuration import EventConfiguration

        d = dict(src_dict)

        def _parse_default_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        default_url = _parse_default_url(d.pop("default_url"))

        def _parse_expires_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)

                return expires_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = EventConfiguration.from_dict(events_item_data)

            events.append(events_item)

        public_key = d.pop("public_key", UNSET)

        webhook_info = cls(
            default_url=default_url,
            expires_at=expires_at,
            events=events,
            public_key=public_key,
        )

        webhook_info.additional_properties = d
        return webhook_info

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
