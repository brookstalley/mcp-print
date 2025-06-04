from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="LayerPosition")


@_attrs_define
class LayerPosition:
    """Information about the Layer position. If the positions are not provided then the design will be automatically
    centered.

        Attributes:
            width (float): Layer width in inches Example: 10.
            height (float): Layer height in inches Example: 10.
            top (float): Layer top position in inches
            left (float): Layer left position in inches
    """

    width: float
    height: float
    top: float
    left: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        top = self.top

        left = self.left

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "width": width,
                "height": height,
                "top": top,
                "left": left,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        width = d.pop("width")

        height = d.pop("height")

        top = d.pop("top")

        left = d.pop("left")

        layer_position = cls(
            width=width,
            height=height,
            top=top,
            left=left,
        )

        layer_position.additional_properties = d
        return layer_position

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
