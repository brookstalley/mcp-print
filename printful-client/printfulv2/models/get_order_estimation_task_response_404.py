from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_order_estimation_task_response_404_error import GetOrderEstimationTaskResponse404Error


T = TypeVar("T", bound="GetOrderEstimationTaskResponse404")


@_attrs_define
class GetOrderEstimationTaskResponse404:
    """
    Attributes:
        data (str): Actual error message Example: Couldn't find order estimation with this UUID..
        error (GetOrderEstimationTaskResponse404Error):
    """

    data: str
    error: "GetOrderEstimationTaskResponse404Error"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data

        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_order_estimation_task_response_404_error import GetOrderEstimationTaskResponse404Error

        d = dict(src_dict)
        data = d.pop("data")

        error = GetOrderEstimationTaskResponse404Error.from_dict(d.pop("error"))

        get_order_estimation_task_response_404 = cls(
            data=data,
            error=error,
        )

        get_order_estimation_task_response_404.additional_properties = d
        return get_order_estimation_task_response_404

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
