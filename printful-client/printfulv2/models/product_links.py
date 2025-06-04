from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hateoas_link import HateoasLink


T = TypeVar("T", bound="ProductLinks")


@_attrs_define
class ProductLinks:
    """HATEOAS links

    Attributes:
        self_ (HateoasLink):
        variants (HateoasLink):
        categories (HateoasLink):
        product_prices (HateoasLink):
        product_sizes (HateoasLink):
        product_images (HateoasLink):
        availability (HateoasLink):
    """

    self_: "HateoasLink"
    variants: "HateoasLink"
    categories: "HateoasLink"
    product_prices: "HateoasLink"
    product_sizes: "HateoasLink"
    product_images: "HateoasLink"
    availability: "HateoasLink"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        variants = self.variants.to_dict()

        categories = self.categories.to_dict()

        product_prices = self.product_prices.to_dict()

        product_sizes = self.product_sizes.to_dict()

        product_images = self.product_images.to_dict()

        availability = self.availability.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "variants": variants,
                "categories": categories,
                "product_prices": product_prices,
                "product_sizes": product_sizes,
                "product_images": product_images,
                "availability": availability,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hateoas_link import HateoasLink

        d = dict(src_dict)
        self_ = HateoasLink.from_dict(d.pop("self"))

        variants = HateoasLink.from_dict(d.pop("variants"))

        categories = HateoasLink.from_dict(d.pop("categories"))

        product_prices = HateoasLink.from_dict(d.pop("product_prices"))

        product_sizes = HateoasLink.from_dict(d.pop("product_sizes"))

        product_images = HateoasLink.from_dict(d.pop("product_images"))

        availability = HateoasLink.from_dict(d.pop("availability"))

        product_links = cls(
            self_=self_,
            variants=variants,
            categories=categories,
            product_prices=product_prices,
            product_sizes=product_sizes,
            product_images=product_images,
            availability=availability,
        )

        product_links.additional_properties = d
        return product_links

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
