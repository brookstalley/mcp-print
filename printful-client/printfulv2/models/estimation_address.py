from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EstimationAddress")


@_attrs_define
class EstimationAddress:
    """Information about the address for estimations.

    Attributes:
        country_code (str): Country code Example: US.
        zip_ (str): ZIP/Postal code Example: 91311.
        state_code (Union[Unset, str]): State code. Example: CA.
    """

    country_code: str
    zip_: str
    state_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country_code = self.country_code

        zip_ = self.zip_

        state_code = self.state_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "country_code": country_code,
                "zip": zip_,
            }
        )
        if state_code is not UNSET:
            field_dict["state_code"] = state_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        country_code = d.pop("country_code")

        zip_ = d.pop("zip")

        state_code = d.pop("state_code", UNSET)

        estimation_address = cls(
            country_code=country_code,
            zip_=zip_,
            state_code=state_code,
        )

        estimation_address.additional_properties = d
        return estimation_address

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
