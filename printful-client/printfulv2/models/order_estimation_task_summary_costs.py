from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.calculation_status import CalculationStatus

T = TypeVar("T", bound="OrderEstimationTaskSummaryCosts")


@_attrs_define
class OrderEstimationTaskSummaryCosts:
    """
    Attributes:
        calculation_status (CalculationStatus): If the costs are being calculated or recalculated, this will have the
            status `calculating`. Once finished the status will be `done`. Example: done.
        currency (Union[None, str]): The code of the currency in which the costs are returned. Example: USD.
        subtotal (Union[None, str]): Total cost of all items. Example: 14.95.
        discount (Union[None, str]): Discount sum. Example: 1.79.
        shipping (Union[None, str]): Shipping costs. Example: 4.79.
        digitization (Union[None, str]): Digitization costs. Example: 3.95.
        additional_fee (Union[None, str]): Additional fee for custom product. Example: 0.00.
        fulfillment_fee (Union[None, str]): Custom product fulfillment fee. Example: 0.00.
        retail_delivery_fee (Union[None, str]): Retail delivery fee. Example: 0.00.
        vat (Union[None, str]): Sum of vat (not included in the item price). Example: 4.60.
        tax (Union[None, str]): Sum of taxes (not included in the item price). Example: 0.00.
        total (Union[None, str]): Grand Total (subtotal-discount+tax+vat+shipping). Example: 26.50.
    """

    calculation_status: CalculationStatus
    currency: Union[None, str]
    subtotal: Union[None, str]
    discount: Union[None, str]
    shipping: Union[None, str]
    digitization: Union[None, str]
    additional_fee: Union[None, str]
    fulfillment_fee: Union[None, str]
    retail_delivery_fee: Union[None, str]
    vat: Union[None, str]
    tax: Union[None, str]
    total: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculation_status = self.calculation_status.value

        currency: Union[None, str]
        currency = self.currency

        subtotal: Union[None, str]
        subtotal = self.subtotal

        discount: Union[None, str]
        discount = self.discount

        shipping: Union[None, str]
        shipping = self.shipping

        digitization: Union[None, str]
        digitization = self.digitization

        additional_fee: Union[None, str]
        additional_fee = self.additional_fee

        fulfillment_fee: Union[None, str]
        fulfillment_fee = self.fulfillment_fee

        retail_delivery_fee: Union[None, str]
        retail_delivery_fee = self.retail_delivery_fee

        vat: Union[None, str]
        vat = self.vat

        tax: Union[None, str]
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
                "digitization": digitization,
                "additional_fee": additional_fee,
                "fulfillment_fee": fulfillment_fee,
                "retail_delivery_fee": retail_delivery_fee,
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

        def _parse_currency(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        currency = _parse_currency(d.pop("currency"))

        def _parse_subtotal(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        subtotal = _parse_subtotal(d.pop("subtotal"))

        def _parse_discount(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        discount = _parse_discount(d.pop("discount"))

        def _parse_shipping(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        shipping = _parse_shipping(d.pop("shipping"))

        def _parse_digitization(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        digitization = _parse_digitization(d.pop("digitization"))

        def _parse_additional_fee(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        additional_fee = _parse_additional_fee(d.pop("additional_fee"))

        def _parse_fulfillment_fee(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        fulfillment_fee = _parse_fulfillment_fee(d.pop("fulfillment_fee"))

        def _parse_retail_delivery_fee(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        retail_delivery_fee = _parse_retail_delivery_fee(d.pop("retail_delivery_fee"))

        def _parse_vat(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        vat = _parse_vat(d.pop("vat"))

        def _parse_tax(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        tax = _parse_tax(d.pop("tax"))

        def _parse_total(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        total = _parse_total(d.pop("total"))

        order_estimation_task_summary_costs = cls(
            calculation_status=calculation_status,
            currency=currency,
            subtotal=subtotal,
            discount=discount,
            shipping=shipping,
            digitization=digitization,
            additional_fee=additional_fee,
            fulfillment_fee=fulfillment_fee,
            retail_delivery_fee=retail_delivery_fee,
            vat=vat,
            tax=tax,
            total=total,
        )

        order_estimation_task_summary_costs.additional_properties = d
        return order_estimation_task_summary_costs

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
