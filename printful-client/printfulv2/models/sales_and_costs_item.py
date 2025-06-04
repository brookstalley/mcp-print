from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SalesAndCostsItem")


@_attrs_define
class SalesAndCostsItem:
    """
    Attributes:
        date (str): The date of the value: day in `Y-m-d` format, month in `Y-m` format or "Total" for the first element
            of the list which shows the total values for the whole requested period
        sales (str): Order retail price data. Available only if retail price fields are properly set up on the
            integration's side
        fulfillment (str): Product fulfillment, digitization, branding, shipping costs and taxes that are charged by
            Printful
        profit (str): The difference between Sales and Fulfillment. If retail price data is not available, profit might
            be negative
        sales_discount (str): Any retail price discounts set up on the integration's side
        fulfillment_discount (str): Any fulfillment discounts (such as the monthly discount) set up on Printful's side
        sales_shipping (str): The retail shipping price that was paid by the buyer
        fulfillment_shipping (str): Shipping costs that were charged by Printful
    """

    date: str
    sales: str
    fulfillment: str
    profit: str
    sales_discount: str
    fulfillment_discount: str
    sales_shipping: str
    fulfillment_shipping: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        sales = self.sales

        fulfillment = self.fulfillment

        profit = self.profit

        sales_discount = self.sales_discount

        fulfillment_discount = self.fulfillment_discount

        sales_shipping = self.sales_shipping

        fulfillment_shipping = self.fulfillment_shipping

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "sales": sales,
                "fulfillment": fulfillment,
                "profit": profit,
                "sales_discount": sales_discount,
                "fulfillment_discount": fulfillment_discount,
                "sales_shipping": sales_shipping,
                "fulfillment_shipping": fulfillment_shipping,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        sales = d.pop("sales")

        fulfillment = d.pop("fulfillment")

        profit = d.pop("profit")

        sales_discount = d.pop("sales_discount")

        fulfillment_discount = d.pop("fulfillment_discount")

        sales_shipping = d.pop("sales_shipping")

        fulfillment_shipping = d.pop("fulfillment_shipping")

        sales_and_costs_item = cls(
            date=date,
            sales=sales,
            fulfillment=fulfillment,
            profit=profit,
            sales_discount=sales_discount,
            fulfillment_discount=fulfillment_discount,
            sales_shipping=sales_shipping,
            fulfillment_shipping=fulfillment_shipping,
        )

        sales_and_costs_item.additional_properties = d
        return sales_and_costs_item

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
