from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_variant_images_by_id_response_200_links_self import GetVariantImagesByIdResponse200LinksSelf
    from ..models.get_variant_images_by_id_response_200_links_variant_details import (
        GetVariantImagesByIdResponse200LinksVariantDetails,
    )


T = TypeVar("T", bound="GetVariantImagesByIdResponse200Links")


@_attrs_define
class GetVariantImagesByIdResponse200Links:
    """HATEOAS links

    Attributes:
        self_ (Union[Unset, GetVariantImagesByIdResponse200LinksSelf]):
        variant_details (Union[Unset, GetVariantImagesByIdResponse200LinksVariantDetails]):
    """

    self_: Union[Unset, "GetVariantImagesByIdResponse200LinksSelf"] = UNSET
    variant_details: Union[Unset, "GetVariantImagesByIdResponse200LinksVariantDetails"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        variant_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.variant_details, Unset):
            variant_details = self.variant_details.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if variant_details is not UNSET:
            field_dict["variant_details"] = variant_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_variant_images_by_id_response_200_links_self import GetVariantImagesByIdResponse200LinksSelf
        from ..models.get_variant_images_by_id_response_200_links_variant_details import (
            GetVariantImagesByIdResponse200LinksVariantDetails,
        )

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, GetVariantImagesByIdResponse200LinksSelf]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = GetVariantImagesByIdResponse200LinksSelf.from_dict(_self_)

        _variant_details = d.pop("variant_details", UNSET)
        variant_details: Union[Unset, GetVariantImagesByIdResponse200LinksVariantDetails]
        if isinstance(_variant_details, Unset):
            variant_details = UNSET
        else:
            variant_details = GetVariantImagesByIdResponse200LinksVariantDetails.from_dict(_variant_details)

        get_variant_images_by_id_response_200_links = cls(
            self_=self_,
            variant_details=variant_details,
        )

        get_variant_images_by_id_response_200_links.additional_properties = d
        return get_variant_images_by_id_response_200_links

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
