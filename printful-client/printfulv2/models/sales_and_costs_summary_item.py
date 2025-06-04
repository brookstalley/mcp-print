from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SalesAndCostsSummaryItem")


@_attrs_define
class SalesAndCostsSummaryItem:
    """
    Attributes:
        date (Union[Unset, str]): The date of the value: day in `Y-m-d` format, month in `Y-m` format or "Total" for the
            first element of the list which shows the total values for the whole requested period
        order_count (Union[Unset, float]): The order count in the aggregation period
        costs (Union[Unset, str]): Product fulfillment, digitization, branding, shipping costs and taxes that are
            charged by Printful
        profit (Union[Unset, str]): The difference between Sales and Fulfillment. If retail price data is not available,
            profit might be negative
    """

    date: Union[Unset, str] = UNSET
    order_count: Union[Unset, float] = UNSET
    costs: Union[Unset, str] = UNSET
    profit: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        order_count = self.order_count

        costs = self.costs

        profit = self.profit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if order_count is not UNSET:
            field_dict["order_count"] = order_count
        if costs is not UNSET:
            field_dict["costs"] = costs
        if profit is not UNSET:
            field_dict["profit"] = profit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date", UNSET)

        order_count = d.pop("order_count", UNSET)

        costs = d.pop("costs", UNSET)

        profit = d.pop("profit", UNSET)

        sales_and_costs_summary_item = cls(
            date=date,
            order_count=order_count,
            costs=costs,
            profit=profit,
        )

        sales_and_costs_summary_item.additional_properties = d
        return sales_and_costs_summary_item

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
