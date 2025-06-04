from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hateoas_link import HateoasLink


T = TypeVar("T", bound="GetCategoryByIdResponse200Links")


@_attrs_define
class GetCategoryByIdResponse200Links:
    """HATEOAS links

    Attributes:
        all_categories (HateoasLink):
    """

    all_categories: "HateoasLink"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_categories = self.all_categories.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "all_categories": all_categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hateoas_link import HateoasLink

        d = dict(src_dict)
        all_categories = HateoasLink.from_dict(d.pop("all_categories"))

        get_category_by_id_response_200_links = cls(
            all_categories=all_categories,
        )

        get_category_by_id_response_200_links.additional_properties = d
        return get_category_by_id_response_200_links

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
