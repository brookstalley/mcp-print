from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetailCosts2")


@_attrs_define
class RetailCosts2:
    """Retail costs

    Attributes:
        currency (Union[Unset, str]): The code of the currency in which the retail costs are returned. Example: EUR.
        discount (Union[Unset, str]): Discount sum. Example: 123.40.
        shipping (Union[Unset, str]): Shipping costs. Example: 123.40.
        tax (Union[Unset, str]): Sum of taxes (not included in the item price). Example: 123.40.
    """

    currency: Union[Unset, str] = UNSET
    discount: Union[Unset, str] = UNSET
    shipping: Union[Unset, str] = UNSET
    tax: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        discount = self.discount

        shipping = self.shipping

        tax = self.tax

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if discount is not UNSET:
            field_dict["discount"] = discount
        if shipping is not UNSET:
            field_dict["shipping"] = shipping
        if tax is not UNSET:
            field_dict["tax"] = tax

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        discount = d.pop("discount", UNSET)

        shipping = d.pop("shipping", UNSET)

        tax = d.pop("tax", UNSET)

        retail_costs_2 = cls(
            currency=currency,
            discount=discount,
            shipping=shipping,
            tax=tax,
        )

        retail_costs_2.additional_properties = d
        return retail_costs_2

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
