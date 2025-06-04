from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PackingSlip")


@_attrs_define
class PackingSlip:
    """The values for customized packing slip

    Attributes:
        email (Union[Unset, str]): Customer service email Example: test@example.com.
        phone (Union[Unset, str]): Customer service phone Example: +48000000000.
        message (Union[Unset, str]): Custom packing slip message Example: This is a message.
        logo_url (Union[Unset, str]): URL address to a sticker we will put on a package Example:
            https://example.com/image.jpg.
        store_name (Union[Unset, str]): Store name override for the return address Example: A store.
        custom_order_id (Union[Unset, str]): Your own Order ID that will be printed instead of Printful's Order ID
            Example: 11235813.
    """

    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    store_name: Union[Unset, str] = UNSET
    custom_order_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        phone = self.phone

        message = self.message

        logo_url = self.logo_url

        store_name = self.store_name

        custom_order_id = self.custom_order_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if message is not UNSET:
            field_dict["message"] = message
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if store_name is not UNSET:
            field_dict["store_name"] = store_name
        if custom_order_id is not UNSET:
            field_dict["custom_order_id"] = custom_order_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        message = d.pop("message", UNSET)

        logo_url = d.pop("logo_url", UNSET)

        store_name = d.pop("store_name", UNSET)

        custom_order_id = d.pop("custom_order_id", UNSET)

        packing_slip = cls(
            email=email,
            phone=phone,
            message=message,
            logo_url=logo_url,
            store_name=store_name,
            custom_order_id=custom_order_id,
        )

        packing_slip.additional_properties = d
        return packing_slip

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
