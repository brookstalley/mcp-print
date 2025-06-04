from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddressReadonly")


@_attrs_define
class AddressReadonly:
    """Information about the address

    Attributes:
        name (str): Full name Example: John Smith.
        company (str): Company name Example: John Smith Inc.
        address1 (str): Address line 1 Example: 19749 Dearborn St.
        address2 (str): Address line 2
        city (str): City Example: Chatsworth.
        state_code (str): State code Example: CA.
        state_name (str): State name Example: California.
        country_code (str): Country code Example: US.
        country_name (str): Country name Example: United States.
        zip_ (str): ZIP/Postal code Example: 91311.
        phone (str): Phone number Example: 2312322334.
        email (str): Email address Example: firstname.secondname@domain.com.
        tax_number (str): TAX number (`optional`, but in case of Brazil country this field becomes `required` and will
            be used as CPF/CNPJ number)<br> CPF format is 000.000.000-00 (14 characters);<br> CNPJ format is
            00.000.000/0000-00 (18 characters). Example: 123.456.789-10.
    """

    name: str
    company: str
    address1: str
    address2: str
    city: str
    state_code: str
    state_name: str
    country_code: str
    country_name: str
    zip_: str
    phone: str
    email: str
    tax_number: str
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
        field_dict.update(
            {
                "name": name,
                "company": company,
                "address1": address1,
                "address2": address2,
                "city": city,
                "state_code": state_code,
                "state_name": state_name,
                "country_code": country_code,
                "country_name": country_name,
                "zip": zip_,
                "phone": phone,
                "email": email,
                "tax_number": tax_number,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        company = d.pop("company")

        address1 = d.pop("address1")

        address2 = d.pop("address2")

        city = d.pop("city")

        state_code = d.pop("state_code")

        state_name = d.pop("state_name")

        country_code = d.pop("country_code")

        country_name = d.pop("country_name")

        zip_ = d.pop("zip")

        phone = d.pop("phone")

        email = d.pop("email")

        tax_number = d.pop("tax_number")

        address_readonly = cls(
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

        address_readonly.additional_properties = d
        return address_readonly

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
