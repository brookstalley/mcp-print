from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PrintfulCosts")


@_attrs_define
class PrintfulCosts:
    """Printful costs report

    Attributes:
        value (str): Amount paid to Printful for fulfillment and shipping.
        relative_difference (Union[None, str]): Relative difference from the value from the previous period. -1 means
            100% decrease, 1 means 100% increase. 0 is returned if there is no change or the previous value was 0.
    """

    value: str
    relative_difference: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value = self.value

        relative_difference: Union[None, str]
        relative_difference = self.relative_difference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "value": value,
                "relative_difference": relative_difference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        def _parse_relative_difference(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        relative_difference = _parse_relative_difference(d.pop("relative_difference"))

        printful_costs = cls(
            value=value,
            relative_difference=relative_difference,
        )

        printful_costs.additional_properties = d
        return printful_costs

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
