from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateMockupProduct")


@_attrs_define
class TemplateMockupProduct:
    """
    Attributes:
        source (str): Mockup product source Example: template.
        product_template_id (int): Product Template identifier Example: 712152512.
        mockup_style_ids (Union[Unset, list[int]]): Used to specify style of mockups that should be generated. For
            example:
              * On the hanger
              * On the Male/Female model
              * Flat on the table
              * etc.
            Available mockup styles for catalog product can be found under _[Retrieve catalog product mockup
            styles](#operation/retrieveMockupStylesByProductId)_.
        catalog_variant_ids (Union[Unset, list[int]]): List of catalog variant identifiers for which mockups will be
            generated. Variants must be defined in the product template specified with `product_template_id`. Multiple
            variants of the same color do not count towards the daily number of files limit. Meaning that for a Red T-Shirt
            of (S,M) sizes we still generate only one mockup.
    """

    source: str
    product_template_id: int
    mockup_style_ids: Union[Unset, list[int]] = UNSET
    catalog_variant_ids: Union[Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        product_template_id = self.product_template_id

        mockup_style_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.mockup_style_ids, Unset):
            mockup_style_ids = self.mockup_style_ids

        catalog_variant_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.catalog_variant_ids, Unset):
            catalog_variant_ids = self.catalog_variant_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "source": source,
                "product_template_id": product_template_id,
            }
        )
        if mockup_style_ids is not UNSET:
            field_dict["mockup_style_ids"] = mockup_style_ids
        if catalog_variant_ids is not UNSET:
            field_dict["catalog_variant_ids"] = catalog_variant_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        product_template_id = d.pop("product_template_id")

        mockup_style_ids = cast(list[int], d.pop("mockup_style_ids", UNSET))

        catalog_variant_ids = cast(list[int], d.pop("catalog_variant_ids", UNSET))

        template_mockup_product = cls(
            source=source,
            product_template_id=product_template_id,
            mockup_style_ids=mockup_style_ids,
            catalog_variant_ids=catalog_variant_ids,
        )

        template_mockup_product.additional_properties = d
        return template_mockup_product

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
