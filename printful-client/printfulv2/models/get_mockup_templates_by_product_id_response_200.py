from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_mockup_templates_by_product_id_response_200_links import (
        GetMockupTemplatesByProductIdResponse200Links,
    )
    from ..models.mockup_templates import MockupTemplates
    from ..models.paging import Paging


T = TypeVar("T", bound="GetMockupTemplatesByProductIdResponse200")


@_attrs_define
class GetMockupTemplatesByProductIdResponse200:
    """
    Attributes:
        data (list['MockupTemplates']):
        field_links (GetMockupTemplatesByProductIdResponse200Links): HATEOAS links
        paging (Union[Unset, Paging]): Paging information
    """

    data: list["MockupTemplates"]
    field_links: "GetMockupTemplatesByProductIdResponse200Links"
    paging: Union[Unset, "Paging"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        field_links = self.field_links.to_dict()

        paging: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "_links": field_links,
            }
        )
        if paging is not UNSET:
            field_dict["paging"] = paging

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_mockup_templates_by_product_id_response_200_links import (
            GetMockupTemplatesByProductIdResponse200Links,
        )
        from ..models.mockup_templates import MockupTemplates
        from ..models.paging import Paging

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MockupTemplates.from_dict(data_item_data)

            data.append(data_item)

        field_links = GetMockupTemplatesByProductIdResponse200Links.from_dict(d.pop("_links"))

        _paging = d.pop("paging", UNSET)
        paging: Union[Unset, Paging]
        if isinstance(_paging, Unset):
            paging = UNSET
        else:
            paging = Paging.from_dict(_paging)

        get_mockup_templates_by_product_id_response_200 = cls(
            data=data,
            field_links=field_links,
            paging=paging,
        )

        get_mockup_templates_by_product_id_response_200.additional_properties = d
        return get_mockup_templates_by_product_id_response_200

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
