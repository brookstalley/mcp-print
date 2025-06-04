from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.average_fulfillment_time import AverageFulfillmentTime
    from ..models.costs_by_amount_item import CostsByAmountItem
    from ..models.costs_by_product_item import CostsByProductItem
    from ..models.costs_by_variant_item import CostsByVariantItem
    from ..models.printful_costs import PrintfulCosts
    from ..models.profit import Profit
    from ..models.sales_and_costs_item import SalesAndCostsItem
    from ..models.sales_and_costs_summary_item import SalesAndCostsSummaryItem
    from ..models.total_paid_orders import TotalPaidOrders


T = TypeVar("T", bound="StoreStatistics")


@_attrs_define
class StoreStatistics:
    """Statistics for a single store

    Attributes:
        store_id (int): The ID of the store for which the statistics are returned
        currency (str): The code of the currency in which the statistics are returned Example: USD.
        sales_and_costs (Union[Unset, list['SalesAndCostsItem']]): Sales and costs report
        sales_and_costs_summary (Union[Unset, list['SalesAndCostsSummaryItem']]): Sales and costs summary report
        printful_costs (Union[Unset, PrintfulCosts]): Printful costs report
        profit (Union[Unset, Profit]): Profit report
        total_paid_orders (Union[Unset, TotalPaidOrders]): Total paid orders report
        costs_by_amount (Union[Unset, list['CostsByAmountItem']]): Costs by amount report
        costs_by_product (Union[Unset, list['CostsByProductItem']]): Costs by product report
        costs_by_variant (Union[Unset, list['CostsByVariantItem']]): Costs by variant report
        average_fulfillment_time (Union[Unset, AverageFulfillmentTime]): Average fulfillment time report
    """

    store_id: int
    currency: str
    sales_and_costs: Union[Unset, list["SalesAndCostsItem"]] = UNSET
    sales_and_costs_summary: Union[Unset, list["SalesAndCostsSummaryItem"]] = UNSET
    printful_costs: Union[Unset, "PrintfulCosts"] = UNSET
    profit: Union[Unset, "Profit"] = UNSET
    total_paid_orders: Union[Unset, "TotalPaidOrders"] = UNSET
    costs_by_amount: Union[Unset, list["CostsByAmountItem"]] = UNSET
    costs_by_product: Union[Unset, list["CostsByProductItem"]] = UNSET
    costs_by_variant: Union[Unset, list["CostsByVariantItem"]] = UNSET
    average_fulfillment_time: Union[Unset, "AverageFulfillmentTime"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        store_id = self.store_id

        currency = self.currency

        sales_and_costs: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sales_and_costs, Unset):
            sales_and_costs = []
            for componentsschemas_sales_and_costs_item_data in self.sales_and_costs:
                componentsschemas_sales_and_costs_item = componentsschemas_sales_and_costs_item_data.to_dict()
                sales_and_costs.append(componentsschemas_sales_and_costs_item)

        sales_and_costs_summary: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sales_and_costs_summary, Unset):
            sales_and_costs_summary = []
            for componentsschemas_sales_and_costs_summary_item_data in self.sales_and_costs_summary:
                componentsschemas_sales_and_costs_summary_item = (
                    componentsschemas_sales_and_costs_summary_item_data.to_dict()
                )
                sales_and_costs_summary.append(componentsschemas_sales_and_costs_summary_item)

        printful_costs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.printful_costs, Unset):
            printful_costs = self.printful_costs.to_dict()

        profit: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profit, Unset):
            profit = self.profit.to_dict()

        total_paid_orders: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.total_paid_orders, Unset):
            total_paid_orders = self.total_paid_orders.to_dict()

        costs_by_amount: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.costs_by_amount, Unset):
            costs_by_amount = []
            for componentsschemas_costs_by_amount_item_data in self.costs_by_amount:
                componentsschemas_costs_by_amount_item = componentsschemas_costs_by_amount_item_data.to_dict()
                costs_by_amount.append(componentsschemas_costs_by_amount_item)

        costs_by_product: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.costs_by_product, Unset):
            costs_by_product = []
            for componentsschemas_costs_by_product_item_data in self.costs_by_product:
                componentsschemas_costs_by_product_item = componentsschemas_costs_by_product_item_data.to_dict()
                costs_by_product.append(componentsschemas_costs_by_product_item)

        costs_by_variant: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.costs_by_variant, Unset):
            costs_by_variant = []
            for componentsschemas_costs_by_variant_item_data in self.costs_by_variant:
                componentsschemas_costs_by_variant_item = componentsschemas_costs_by_variant_item_data.to_dict()
                costs_by_variant.append(componentsschemas_costs_by_variant_item)

        average_fulfillment_time: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.average_fulfillment_time, Unset):
            average_fulfillment_time = self.average_fulfillment_time.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "store_id": store_id,
                "currency": currency,
            }
        )
        if sales_and_costs is not UNSET:
            field_dict["sales_and_costs"] = sales_and_costs
        if sales_and_costs_summary is not UNSET:
            field_dict["sales_and_costs_summary"] = sales_and_costs_summary
        if printful_costs is not UNSET:
            field_dict["printful_costs"] = printful_costs
        if profit is not UNSET:
            field_dict["profit"] = profit
        if total_paid_orders is not UNSET:
            field_dict["total_paid_orders"] = total_paid_orders
        if costs_by_amount is not UNSET:
            field_dict["costs_by_amount"] = costs_by_amount
        if costs_by_product is not UNSET:
            field_dict["costs_by_product"] = costs_by_product
        if costs_by_variant is not UNSET:
            field_dict["costs_by_variant"] = costs_by_variant
        if average_fulfillment_time is not UNSET:
            field_dict["average_fulfillment_time"] = average_fulfillment_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.average_fulfillment_time import AverageFulfillmentTime
        from ..models.costs_by_amount_item import CostsByAmountItem
        from ..models.costs_by_product_item import CostsByProductItem
        from ..models.costs_by_variant_item import CostsByVariantItem
        from ..models.printful_costs import PrintfulCosts
        from ..models.profit import Profit
        from ..models.sales_and_costs_item import SalesAndCostsItem
        from ..models.sales_and_costs_summary_item import SalesAndCostsSummaryItem
        from ..models.total_paid_orders import TotalPaidOrders

        d = dict(src_dict)
        store_id = d.pop("store_id")

        currency = d.pop("currency")

        sales_and_costs = []
        _sales_and_costs = d.pop("sales_and_costs", UNSET)
        for componentsschemas_sales_and_costs_item_data in _sales_and_costs or []:
            componentsschemas_sales_and_costs_item = SalesAndCostsItem.from_dict(
                componentsschemas_sales_and_costs_item_data
            )

            sales_and_costs.append(componentsschemas_sales_and_costs_item)

        sales_and_costs_summary = []
        _sales_and_costs_summary = d.pop("sales_and_costs_summary", UNSET)
        for componentsschemas_sales_and_costs_summary_item_data in _sales_and_costs_summary or []:
            componentsschemas_sales_and_costs_summary_item = SalesAndCostsSummaryItem.from_dict(
                componentsschemas_sales_and_costs_summary_item_data
            )

            sales_and_costs_summary.append(componentsschemas_sales_and_costs_summary_item)

        _printful_costs = d.pop("printful_costs", UNSET)
        printful_costs: Union[Unset, PrintfulCosts]
        if isinstance(_printful_costs, Unset):
            printful_costs = UNSET
        else:
            printful_costs = PrintfulCosts.from_dict(_printful_costs)

        _profit = d.pop("profit", UNSET)
        profit: Union[Unset, Profit]
        if isinstance(_profit, Unset):
            profit = UNSET
        else:
            profit = Profit.from_dict(_profit)

        _total_paid_orders = d.pop("total_paid_orders", UNSET)
        total_paid_orders: Union[Unset, TotalPaidOrders]
        if isinstance(_total_paid_orders, Unset):
            total_paid_orders = UNSET
        else:
            total_paid_orders = TotalPaidOrders.from_dict(_total_paid_orders)

        costs_by_amount = []
        _costs_by_amount = d.pop("costs_by_amount", UNSET)
        for componentsschemas_costs_by_amount_item_data in _costs_by_amount or []:
            componentsschemas_costs_by_amount_item = CostsByAmountItem.from_dict(
                componentsschemas_costs_by_amount_item_data
            )

            costs_by_amount.append(componentsschemas_costs_by_amount_item)

        costs_by_product = []
        _costs_by_product = d.pop("costs_by_product", UNSET)
        for componentsschemas_costs_by_product_item_data in _costs_by_product or []:
            componentsschemas_costs_by_product_item = CostsByProductItem.from_dict(
                componentsschemas_costs_by_product_item_data
            )

            costs_by_product.append(componentsschemas_costs_by_product_item)

        costs_by_variant = []
        _costs_by_variant = d.pop("costs_by_variant", UNSET)
        for componentsschemas_costs_by_variant_item_data in _costs_by_variant or []:
            componentsschemas_costs_by_variant_item = CostsByVariantItem.from_dict(
                componentsschemas_costs_by_variant_item_data
            )

            costs_by_variant.append(componentsschemas_costs_by_variant_item)

        _average_fulfillment_time = d.pop("average_fulfillment_time", UNSET)
        average_fulfillment_time: Union[Unset, AverageFulfillmentTime]
        if isinstance(_average_fulfillment_time, Unset):
            average_fulfillment_time = UNSET
        else:
            average_fulfillment_time = AverageFulfillmentTime.from_dict(_average_fulfillment_time)

        store_statistics = cls(
            store_id=store_id,
            currency=currency,
            sales_and_costs=sales_and_costs,
            sales_and_costs_summary=sales_and_costs_summary,
            printful_costs=printful_costs,
            profit=profit,
            total_paid_orders=total_paid_orders,
            costs_by_amount=costs_by_amount,
            costs_by_product=costs_by_product,
            costs_by_variant=costs_by_variant,
            average_fulfillment_time=average_fulfillment_time,
        )

        store_statistics.additional_properties = d
        return store_statistics

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
