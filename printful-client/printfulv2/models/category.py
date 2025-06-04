from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.category_links import CategoryLinks


T = TypeVar("T", bound="Category")


@_attrs_define
class Category:
    """Information about the Category

    Attributes:
        id (int): Category ID Example: 24.
        parent_id (Union[None, int]): ID of the parent Category. If there is no parent Category, null is returned.
            Example: 6.
        image_url (str): The URL of the Category image Example: https://s3-
            printful.stage.printful.dev/upload/catalog_category/b1/b1513c82696405fcc316fc611c57f132_t?v=1646395980.
        title (str): Category title Example: T-Shirts.
        field_links (CategoryLinks): HATEOAS links
    """

    id: int
    parent_id: Union[None, int]
    image_url: str
    title: str
    field_links: "CategoryLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent_id: Union[None, int]
        parent_id = self.parent_id

        image_url = self.image_url

        title = self.title

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "parent_id": parent_id,
                "image_url": image_url,
                "title": title,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.category_links import CategoryLinks

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_parent_id(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        parent_id = _parse_parent_id(d.pop("parent_id"))

        image_url = d.pop("image_url")

        title = d.pop("title")

        field_links = CategoryLinks.from_dict(d.pop("_links"))

        category = cls(
            id=id,
            parent_id=parent_id,
            image_url=image_url,
            title=title,
            field_links=field_links,
        )

        category.additional_properties = d
        return category

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
