from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_product_variants_by_id_response_200_links import GetProductVariantsByIdResponse200Links
    from ..models.paging import Paging
    from ..models.variant import Variant


T = TypeVar("T", bound="GetProductVariantsByIdResponse200")


@_attrs_define
class GetProductVariantsByIdResponse200:
    """
    Attributes:
        data (list['Variant']):
        paging (Paging): Paging information
        field_links (GetProductVariantsByIdResponse200Links): HATEOAS links
    """

    data: list["Variant"]
    paging: "Paging"
    field_links: "GetProductVariantsByIdResponse200Links"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        paging = self.paging.to_dict()

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "paging": paging,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_variants_by_id_response_200_links import GetProductVariantsByIdResponse200Links
        from ..models.paging import Paging
        from ..models.variant import Variant

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Variant.from_dict(data_item_data)

            data.append(data_item)

        paging = Paging.from_dict(d.pop("paging"))

        field_links = GetProductVariantsByIdResponse200Links.from_dict(d.pop("_links"))

        get_product_variants_by_id_response_200 = cls(
            data=data,
            paging=paging,
            field_links=field_links,
        )

        get_product_variants_by_id_response_200.additional_properties = d
        return get_product_variants_by_id_response_200

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
