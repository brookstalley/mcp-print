from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hateoas_link import HateoasLink


T = TypeVar("T", bound="GetProductSizeGuideByIdResponse200Links")


@_attrs_define
class GetProductSizeGuideByIdResponse200Links:
    """HATEOAS links

    Attributes:
        self_ (HateoasLink):
        product_details (HateoasLink):
    """

    self_: "HateoasLink"
    product_details: "HateoasLink"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        product_details = self.product_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
                "product_details": product_details,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hateoas_link import HateoasLink

        d = dict(src_dict)
        self_ = HateoasLink.from_dict(d.pop("self"))

        product_details = HateoasLink.from_dict(d.pop("product_details"))

        get_product_size_guide_by_id_response_200_links = cls(
            self_=self_,
            product_details=product_details,
        )

        get_product_size_guide_by_id_response_200_links.additional_properties = d
        return get_product_size_guide_by_id_response_200_links

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
