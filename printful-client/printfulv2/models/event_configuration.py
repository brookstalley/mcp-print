from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_configuration_event_param import EventConfigurationEventParam


T = TypeVar("T", bound="EventConfiguration")


@_attrs_define
class EventConfiguration:
    """
    Attributes:
        type_ (str): Event type. Example: catalog_stock_updated.
        url (Union[None, Unset, str]): Webhook URL (HTTPS-only) that will receive the event notifications. Example:
            ​https://www.example.com/printful/webhook.
        params (Union[Unset, list['EventConfigurationEventParam']]):  Example: [{'name': 'products', 'value': [{'id':
            1}, {'id': 71}]}].
    """

    type_: str
    url: Union[None, Unset, str] = UNSET
    params: Union[Unset, list["EventConfigurationEventParam"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        params: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.params, Unset):
            params = []
            for params_item_data in self.params:
                params_item = params_item_data.to_dict()
                params.append(params_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_configuration_event_param import EventConfigurationEventParam

        d = dict(src_dict)
        type_ = d.pop("type")

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        params = []
        _params = d.pop("params", UNSET)
        for params_item_data in _params or []:
            params_item = EventConfigurationEventParam.from_dict(params_item_data)

            params.append(params_item)

        event_configuration = cls(
            type_=type_,
            url=url,
            params=params,
        )

        event_configuration.additional_properties = d
        return event_configuration

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
