from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mockup import Mockup


T = TypeVar("T", bound="MockupGeneratorTaskCatalogVariantMockupsItem")


@_attrs_define
class MockupGeneratorTaskCatalogVariantMockupsItem:
    """
    Attributes:
        catalog_variant_id (int): ID of a catalog variant for which the mockup was generated. Example: 4011.
        mockups (list['Mockup']): List of generated mockups
    """

    catalog_variant_id: int
    mockups: list["Mockup"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_variant_id = self.catalog_variant_id

        mockups = []
        for mockups_item_data in self.mockups:
            mockups_item = mockups_item_data.to_dict()
            mockups.append(mockups_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_variant_id": catalog_variant_id,
                "mockups": mockups,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mockup import Mockup

        d = dict(src_dict)
        catalog_variant_id = d.pop("catalog_variant_id")

        mockups = []
        _mockups = d.pop("mockups")
        for mockups_item_data in _mockups:
            mockups_item = Mockup.from_dict(mockups_item_data)

            mockups.append(mockups_item)

        mockup_generator_task_catalog_variant_mockups_item = cls(
            catalog_variant_id=catalog_variant_id,
            mockups=mockups,
        )

        mockup_generator_task_catalog_variant_mockups_item.additional_properties = d
        return mockup_generator_task_catalog_variant_mockups_item

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
