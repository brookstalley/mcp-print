from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PackingSlipReadonly")


@_attrs_define
class PackingSlipReadonly:
    """The values for customized packing slip

    Attributes:
        email (str): Customer service email Example: test@example.com.
        phone (str): Customer service phone Example: +48000000000.
        message (str): Custom packing slip message Example: This is a message.
        logo_url (str): URL address to a sticker we will put on a package Example: https://example.com/image.jpg.
        store_name (str): Store name override for the return address Example: A store.
        custom_order_id (str): Your own Order ID that will be printed instead of Printful's Order ID Example: 11235813.
    """

    email: str
    phone: str
    message: str
    logo_url: str
    store_name: str
    custom_order_id: str
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
        field_dict.update(
            {
                "email": email,
                "phone": phone,
                "message": message,
                "logo_url": logo_url,
                "store_name": store_name,
                "custom_order_id": custom_order_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        phone = d.pop("phone")

        message = d.pop("message")

        logo_url = d.pop("logo_url")

        store_name = d.pop("store_name")

        custom_order_id = d.pop("custom_order_id")

        packing_slip_readonly = cls(
            email=email,
            phone=phone,
            message=message,
            logo_url=logo_url,
            store_name=store_name,
            custom_order_id=custom_order_id,
        )

        packing_slip_readonly.additional_properties = d
        return packing_slip_readonly

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
