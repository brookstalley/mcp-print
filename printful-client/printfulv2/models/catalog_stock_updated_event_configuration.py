from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.products_param import ProductsParam


T = TypeVar("T", bound="CatalogStockUpdatedEventConfiguration")


@_attrs_define
class CatalogStockUpdatedEventConfiguration:
    """
    Attributes:
        type_ (str): Event type. The dropdown shows values required for webhook event configuration. During the setup of
            a new webhook
            event please check this dropdown if the event does not require additional parameters to be set.
             Example: shipment_sent.
        params (list['ProductsParam']):  Example: [{'name': 'products', 'value': [{'id': 1}, {'id': 71}]}].
        url (Union[None, Unset, str]): Webhook URL (HTTPS-only) that will receive the event notifications. Example:
            ​https://www.example.com/printful/webhook.
    """

    type_: str
    params: list["ProductsParam"]
    url: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        params = []
        for params_item_data in self.params:
            params_item = params_item_data.to_dict()
            params.append(params_item)

        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "params": params,
            }
        )
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.products_param import ProductsParam

        d = dict(src_dict)
        type_ = d.pop("type")

        params = []
        _params = d.pop("params")
        for params_item_data in _params:
            params_item = ProductsParam.from_dict(params_item_data)

            params.append(params_item)

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        catalog_stock_updated_event_configuration = cls(
            type_=type_,
            params=params,
            url=url,
        )

        catalog_stock_updated_event_configuration.additional_properties = d
        return catalog_stock_updated_event_configuration

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
