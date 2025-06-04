from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hateoas_link import HateoasLink


T = TypeVar("T", bound="GetVariantByIdResponse200Links")


@_attrs_define
class GetVariantByIdResponse200Links:
    """HATEOAS links

    Attributes:
        self_ (HateoasLink):
        product_variants (HateoasLink):
        product_details (HateoasLink):
        variant_prices (HateoasLink):
        variant_images (HateoasLink):
    """

    self_: "HateoasLink"
    product_variants: "HateoasLink"
    product_details: "HateoasLink"
    variant_prices: "HateoasLink"
    variant_images: "HateoasLink"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        product_variants = self.product_variants.to_dict()

        product_details = self.product_details.to_dict()

        variant_prices = self.variant_prices.to_dict()

        variant_images = self.variant_images.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "product_variants": product_variants,
                "product_details": product_details,
                "variant_prices": variant_prices,
                "variant_images": variant_images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hateoas_link import HateoasLink

        d = dict(src_dict)
        self_ = HateoasLink.from_dict(d.pop("self"))

        product_variants = HateoasLink.from_dict(d.pop("product_variants"))

        product_details = HateoasLink.from_dict(d.pop("product_details"))

        variant_prices = HateoasLink.from_dict(d.pop("variant_prices"))

        variant_images = HateoasLink.from_dict(d.pop("variant_images"))

        get_variant_by_id_response_200_links = cls(
            self_=self_,
            product_variants=product_variants,
            product_details=product_details,
            variant_prices=variant_prices,
            variant_images=variant_images,
        )

        get_variant_by_id_response_200_links.additional_properties = d
        return get_variant_by_id_response_200_links

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
