from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mockup_generator_task_status import MockupGeneratorTaskStatus

if TYPE_CHECKING:
    from ..models.error import Error
    from ..models.mockup_generator_task_catalog_variant_mockups_item import MockupGeneratorTaskCatalogVariantMockupsItem
    from ..models.mockup_generator_task_links import MockupGeneratorTaskLinks


T = TypeVar("T", bound="MockupGeneratorTask")


@_attrs_define
class MockupGeneratorTask:
    """Result of mockup generator task

    Attributes:
        id (int): Unique task identifier used to check status of the task and retrieve the results once the task is
            ready. Example: 597350033.
        status (MockupGeneratorTaskStatus): Task status:
             * `completed` – Mockup Generator task was successfully processed
             * `pending` – Mockup Generator task is still being processed
             * `failed` – Mockup Generator task failed
        catalog_variant_mockups (list['MockupGeneratorTaskCatalogVariantMockupsItem']): A list of mockups grouped by
            variant. Note that the same list of mockups can appear under multiple variants, this happens in cases where the
            variants have the same mockups, for example if the only difference is the size of the variant.
        failure_reasons (list['Error']):
        field_links (MockupGeneratorTaskLinks): HATEOAS links
    """

    id: int
    status: MockupGeneratorTaskStatus
    catalog_variant_mockups: list["MockupGeneratorTaskCatalogVariantMockupsItem"]
    failure_reasons: list["Error"]
    field_links: "MockupGeneratorTaskLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status.value

        catalog_variant_mockups = []
        for catalog_variant_mockups_item_data in self.catalog_variant_mockups:
            catalog_variant_mockups_item = catalog_variant_mockups_item_data.to_dict()
            catalog_variant_mockups.append(catalog_variant_mockups_item)

        failure_reasons = []
        for failure_reasons_item_data in self.failure_reasons:
            failure_reasons_item = failure_reasons_item_data.to_dict()
            failure_reasons.append(failure_reasons_item)

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "catalog_variant_mockups": catalog_variant_mockups,
                "failure_reasons": failure_reasons,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error import Error
        from ..models.mockup_generator_task_catalog_variant_mockups_item import (
            MockupGeneratorTaskCatalogVariantMockupsItem,
        )
        from ..models.mockup_generator_task_links import MockupGeneratorTaskLinks

        d = dict(src_dict)
        id = d.pop("id")

        status = MockupGeneratorTaskStatus(d.pop("status"))

        catalog_variant_mockups = []
        _catalog_variant_mockups = d.pop("catalog_variant_mockups")
        for catalog_variant_mockups_item_data in _catalog_variant_mockups:
            catalog_variant_mockups_item = MockupGeneratorTaskCatalogVariantMockupsItem.from_dict(
                catalog_variant_mockups_item_data
            )

            catalog_variant_mockups.append(catalog_variant_mockups_item)

        failure_reasons = []
        _failure_reasons = d.pop("failure_reasons")
        for failure_reasons_item_data in _failure_reasons:
            failure_reasons_item = Error.from_dict(failure_reasons_item_data)

            failure_reasons.append(failure_reasons_item)

        field_links = MockupGeneratorTaskLinks.from_dict(d.pop("_links"))

        mockup_generator_task = cls(
            id=id,
            status=status,
            catalog_variant_mockups=catalog_variant_mockups,
            failure_reasons=failure_reasons,
            field_links=field_links,
        )

        mockup_generator_task.additional_properties = d
        return mockup_generator_task

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
