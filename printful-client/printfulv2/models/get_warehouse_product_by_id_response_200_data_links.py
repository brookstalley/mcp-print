from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hateoas_link import HateoasLink


T = TypeVar("T", bound="GetWarehouseProductByIdResponse200DataLinks")


@_attrs_define
class GetWarehouseProductByIdResponse200DataLinks:
    """Links to related resources

    Attributes:
        self_ (Union[Unset, HateoasLink]):
        warehouse_variants (Union[Unset, HateoasLink]):
    """

    self_: Union[Unset, "HateoasLink"] = UNSET
    warehouse_variants: Union[Unset, "HateoasLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_, Unset):
            self_ = self.self_.to_dict()

        warehouse_variants: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.warehouse_variants, Unset):
            warehouse_variants = self.warehouse_variants.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if warehouse_variants is not UNSET:
            field_dict["warehouse_variants"] = warehouse_variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hateoas_link import HateoasLink

        d = dict(src_dict)
        _self_ = d.pop("self", UNSET)
        self_: Union[Unset, HateoasLink]
        if isinstance(_self_, Unset):
            self_ = UNSET
        else:
            self_ = HateoasLink.from_dict(_self_)

        _warehouse_variants = d.pop("warehouse_variants", UNSET)
        warehouse_variants: Union[Unset, HateoasLink]
        if isinstance(_warehouse_variants, Unset):
            warehouse_variants = UNSET
        else:
            warehouse_variants = HateoasLink.from_dict(_warehouse_variants)

        get_warehouse_product_by_id_response_200_data_links = cls(
            self_=self_,
            warehouse_variants=warehouse_variants,
        )

        get_warehouse_product_by_id_response_200_data_links.additional_properties = d
        return get_warehouse_product_by_id_response_200_data_links

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
