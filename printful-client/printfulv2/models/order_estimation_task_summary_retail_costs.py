from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calculation_status import CalculationStatus

T = TypeVar("T", bound="OrderEstimationTaskSummaryRetailCosts")


@_attrs_define
class OrderEstimationTaskSummaryRetailCosts:
    """
    Attributes:
        calculation_status (CalculationStatus): If the costs are being calculated or recalculated, this will have the
            status `calculating`. Once finished the status will be `done`. Example: done.
        currency (str): The code of the currency in which the retail costs are returned. Example: EUR.
        subtotal (Union[None, str]): Total cost of all items. Example: 26.55.
        discount (str): Discount sum. Example: 0.00.
        shipping (str): Shipping costs. Example: 4.79.
        vat (str): Sum of VAT (not included in the item price). Example: 0.00.
        tax (str): Sum of taxes (not included in the item price). Example: 0.00.
        total (Union[None, str]): Grand Total (subtotal-discount+tax+vat+shipping). Example: 31.34.
    """

    calculation_status: CalculationStatus
    currency: str
    subtotal: Union[None, str]
    discount: str
    shipping: str
    vat: str
    tax: str
    total: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculation_status = self.calculation_status.value

        currency = self.currency

        subtotal: Union[None, str]
        subtotal = self.subtotal

        discount = self.discount

        shipping = self.shipping

        vat = self.vat

        tax = self.tax

        total: Union[None, str]
        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculation_status": calculation_status,
                "currency": currency,
                "subtotal": subtotal,
                "discount": discount,
                "shipping": shipping,
                "vat": vat,
                "tax": tax,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculation_status = CalculationStatus(d.pop("calculation_status"))

        currency = d.pop("currency")

        def _parse_subtotal(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subtotal = _parse_subtotal(d.pop("subtotal"))

        discount = d.pop("discount")

        shipping = d.pop("shipping")

        vat = d.pop("vat")

        tax = d.pop("tax")

        def _parse_total(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        total = _parse_total(d.pop("total"))

        order_estimation_task_summary_retail_costs = cls(
            calculation_status=calculation_status,
            currency=currency,
            subtotal=subtotal,
            discount=discount,
            shipping=shipping,
            vat=vat,
            tax=tax,
            total=total,
        )

        order_estimation_task_summary_retail_costs.additional_properties = d
        return order_estimation_task_summary_retail_costs

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
