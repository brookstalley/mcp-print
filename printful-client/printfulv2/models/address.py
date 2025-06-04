from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """Information about the address

    Attributes:
        name (Union[Unset, str]): Full name Example: John Smith.
        company (Union[Unset, str]): Company name Example: John Smith Inc.
        address1 (Union[Unset, str]): Address line 1 Example: 19749 Dearborn St.
        address2 (Union[Unset, str]): Address line 2
        city (Union[Unset, str]): City Example: Chatsworth.
        state_code (Union[Unset, str]): State code Example: CA.
        state_name (Union[Unset, str]): State name Example: California.
        country_code (Union[Unset, str]): Country code Example: US.
        country_name (Union[Unset, str]): Country name Example: United States.
        zip_ (Union[Unset, str]): ZIP/Postal code Example: 91311.
        phone (Union[Unset, str]): Phone number Example: 2312322334.
        email (Union[Unset, str]): Email address Example: firstname.secondname@domain.com.
        tax_number (Union[Unset, str]): TAX number (`optional`, but in case of Brazil country this field becomes
            `required` and will be used as CPF/CNPJ number)<br> CPF format is 000.000.000-00 (14 characters);<br> CNPJ
            format is 00.000.000/0000-00 (18 characters). Example: 123.456.789-10.
    """

    name: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    address1: Union[Unset, str] = UNSET
    address2: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    state_name: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    country_name: Union[Unset, str] = UNSET
    zip_: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    tax_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        company = self.company

        address1 = self.address1

        address2 = self.address2

        city = self.city

        state_code = self.state_code

        state_name = self.state_name

        country_code = self.country_code

        country_name = self.country_name

        zip_ = self.zip_

        phone = self.phone

        email = self.email

        tax_number = self.tax_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if company is not UNSET:
            field_dict["company"] = company
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if city is not UNSET:
            field_dict["city"] = city
        if state_code is not UNSET:
            field_dict["state_code"] = state_code
        if state_name is not UNSET:
            field_dict["state_name"] = state_name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if zip_ is not UNSET:
            field_dict["zip"] = zip_
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if tax_number is not UNSET:
            field_dict["tax_number"] = tax_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        company = d.pop("company", UNSET)

        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        city = d.pop("city", UNSET)

        state_code = d.pop("state_code", UNSET)

        state_name = d.pop("state_name", UNSET)

        country_code = d.pop("country_code", UNSET)

        country_name = d.pop("country_name", UNSET)

        zip_ = d.pop("zip", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        tax_number = d.pop("tax_number", UNSET)

        address = cls(
            name=name,
            company=company,
            address1=address1,
            address2=address2,
            city=city,
            state_code=state_code,
            state_name=state_name,
            country_code=country_code,
            country_name=country_name,
            zip_=zip_,
            phone=phone,
            email=email,
            tax_number=tax_number,
        )

        address.additional_properties = d
        return address

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
