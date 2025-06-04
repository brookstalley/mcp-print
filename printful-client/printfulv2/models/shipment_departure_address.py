from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipmentDepartureAddress")


@_attrs_define
class ShipmentDepartureAddress:
    """
    Attributes:
        country_name (Union[Unset, str]):  Example: United States.
        country_code (Union[Unset, str]):  Example: US.
        state_code (Union[Unset, str]):  Example: CA.
    """

    country_name: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_name = self.country_name

        country_code = self.country_code

        state_code = self.state_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country_name is not UNSET:
            field_dict["country_name"] = country_name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if state_code is not UNSET:
            field_dict["state_code"] = state_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_name = d.pop("country_name", UNSET)

        country_code = d.pop("country_code", UNSET)

        state_code = d.pop("state_code", UNSET)

        shipment_departure_address = cls(
            country_name=country_name,
            country_code=country_code,
            state_code=state_code,
        )

        shipment_departure_address.additional_properties = d
        return shipment_departure_address

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
