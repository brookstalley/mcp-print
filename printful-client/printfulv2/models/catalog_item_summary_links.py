from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_item_summary_links_self import CatalogItemSummaryLinksSelf


T = TypeVar("T", bound="CatalogItemSummaryLinks")


@_attrs_define
class CatalogItemSummaryLinks:
    """HATEOAS links

    Attributes:
        self_ (CatalogItemSummaryLinksSelf):
    """

    self_: "CatalogItemSummaryLinksSelf"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_item_summary_links_self import CatalogItemSummaryLinksSelf

        d = dict(src_dict)
        self_ = CatalogItemSummaryLinksSelf.from_dict(d.pop("self"))

        catalog_item_summary_links = cls(
            self_=self_,
        )

        catalog_item_summary_links.additional_properties = d
        return catalog_item_summary_links

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
