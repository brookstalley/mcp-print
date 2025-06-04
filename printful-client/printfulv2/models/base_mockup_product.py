from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BaseMockupProduct")


@_attrs_define
class BaseMockupProduct:
    """
    Attributes:
        source (str): Mockup product source Example: catalog.
        mockup_style_ids (Union[Unset, list[int]]): Used to specify style of mockups that should be generated. For
            example:
              * On the hanger
              * On the Male/Female model
              * Flat on the table
              * etc.
            Available mockup styles for catalog product can be found under _[Retrieve catalog product mockup
            styles](#operation/retrieveMockupStylesByProductId)_.
    """

    source: str
    mockup_style_ids: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        mockup_style_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.mockup_style_ids, Unset):
            mockup_style_ids = self.mockup_style_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
            }
        )
        if mockup_style_ids is not UNSET:
            field_dict["mockup_style_ids"] = mockup_style_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        mockup_style_ids = cast(list[int], d.pop("mockup_style_ids", UNSET))

        base_mockup_product = cls(
            source=source,
            mockup_style_ids=mockup_style_ids,
        )

        base_mockup_product.additional_properties = d
        return base_mockup_product

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
