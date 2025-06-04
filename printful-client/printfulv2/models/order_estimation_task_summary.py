from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.order_estimation_task_summary_status import OrderEstimationTaskSummaryStatus

if TYPE_CHECKING:
    from ..models.order_estimation_task_summary_costs import OrderEstimationTaskSummaryCosts
    from ..models.order_estimation_task_summary_retail_costs import OrderEstimationTaskSummaryRetailCosts


T = TypeVar("T", bound="OrderEstimationTaskSummary")


@_attrs_define
class OrderEstimationTaskSummary:
    """Order estimation task summary

    Attributes:
        id (str): Task ID Example: fc959efb-b3a0-4c12-9cc6-f54d3158291d.
        status (OrderEstimationTaskSummaryStatus): Task status
        costs (OrderEstimationTaskSummaryCosts):
        retail_costs (OrderEstimationTaskSummaryRetailCosts):
        failure_reasons (list[str]): Reasons why calculation failed.
    """

    id: str
    status: OrderEstimationTaskSummaryStatus
    costs: "OrderEstimationTaskSummaryCosts"
    retail_costs: "OrderEstimationTaskSummaryRetailCosts"
    failure_reasons: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        costs = self.costs.to_dict()

        retail_costs = self.retail_costs.to_dict()

        failure_reasons = self.failure_reasons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "costs": costs,
                "retail_costs": retail_costs,
                "failure_reasons": failure_reasons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.order_estimation_task_summary_costs import OrderEstimationTaskSummaryCosts
        from ..models.order_estimation_task_summary_retail_costs import OrderEstimationTaskSummaryRetailCosts

        d = dict(src_dict)
        id = d.pop("id")

        status = OrderEstimationTaskSummaryStatus(d.pop("status"))

        costs = OrderEstimationTaskSummaryCosts.from_dict(d.pop("costs"))

        retail_costs = OrderEstimationTaskSummaryRetailCosts.from_dict(d.pop("retail_costs"))

        failure_reasons = cast(list[str], d.pop("failure_reasons"))

        order_estimation_task_summary = cls(
            id=id,
            status=status,
            costs=costs,
            retail_costs=retail_costs,
            failure_reasons=failure_reasons,
        )

        order_estimation_task_summary.additional_properties = d
        return order_estimation_task_summary

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
