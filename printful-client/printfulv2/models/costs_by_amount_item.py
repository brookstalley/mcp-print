from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CostsByAmountItem")


@_attrs_define
class CostsByAmountItem:
    """
    Attributes:
        date (str): The date of the value: day in `Y-m-d` format, month in `Y-m` format or "Total" for the first element
            of the list which shows the total values for the whole requested period
        product_amount (str): Product & fulfillment costs
        digitization (str): Embroidery digitization costs
        branding (str): Pack-in costs
        vat (str): Tax amounts. If not applicable, it will be 0.
        sales_tax (str): Tax amounts. If not applicable, it will be 0.
        shipping (str): Shipping costs that were charged by Printful
        discount (str): Any fulfillment discounts (such as the monthly discount) set up on Printful's side
        total (str): Summary of all costs
    """

    date: str
    product_amount: str
    digitization: str
    branding: str
    vat: str
    sales_tax: str
    shipping: str
    discount: str
    total: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        product_amount = self.product_amount

        digitization = self.digitization

        branding = self.branding

        vat = self.vat

        sales_tax = self.sales_tax

        shipping = self.shipping

        discount = self.discount

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "product_amount": product_amount,
                "digitization": digitization,
                "branding": branding,
                "vat": vat,
                "sales_tax": sales_tax,
                "shipping": shipping,
                "discount": discount,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        product_amount = d.pop("product_amount")

        digitization = d.pop("digitization")

        branding = d.pop("branding")

        vat = d.pop("vat")

        sales_tax = d.pop("sales_tax")

        shipping = d.pop("shipping")

        discount = d.pop("discount")

        total = d.pop("total")

        costs_by_amount_item = cls(
            date=date,
            product_amount=product_amount,
            digitization=digitization,
            branding=branding,
            vat=vat,
            sales_tax=sales_tax,
            shipping=shipping,
            discount=discount,
            total=total,
        )

        costs_by_amount_item.additional_properties = d
        return costs_by_amount_item

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
