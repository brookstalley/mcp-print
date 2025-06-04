from enum import Enum


class GetReportsReportTypes(str, Enum):
    AVERAGE_FULFILLMENT_TYPE = "average_fulfillment_type"
    COSTS_BY_AMOUNT = "costs_by_amount"
    COSTS_BY_PRODUCT = "costs_by_product"
    COSTS_BY_VARIANT = "costs_by_variant"
    PRINTFUL_COSTS = "printful_costs"
    PROFIT = "profit"
    SALES_AND_COSTS = "sales_and_costs"
    SALES_AND_COSTS_SUMMARY = "sales_and_costs_summary"
    TOTAL_PAID_ORDERS = "total_paid_orders"

    def __str__(self) -> str:
        return str(self.value)
