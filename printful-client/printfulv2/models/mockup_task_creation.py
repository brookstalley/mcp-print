from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mockup_task_creation_format import MockupTaskCreationFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_mockup_product import CatalogMockupProduct
    from ..models.template_mockup_product import TemplateMockupProduct


T = TypeVar("T", bound="MockupTaskCreation")


@_attrs_define
class MockupTaskCreation:
    """
    Attributes:
        products (list[Union['CatalogMockupProduct', 'TemplateMockupProduct']]):
        format_ (Union[Unset, MockupTaskCreationFormat]): Generated file format. PNG will have a transparent background,
            JPG will have a smaller file size.
    """

    products: list[Union["CatalogMockupProduct", "TemplateMockupProduct"]]
    format_: Union[Unset, MockupTaskCreationFormat] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_mockup_product import CatalogMockupProduct

        products = []
        for products_item_data in self.products:
            products_item: dict[str, Any]
            if isinstance(products_item_data, CatalogMockupProduct):
                products_item = products_item_data.to_dict()
            else:
                products_item = products_item_data.to_dict()

            products.append(products_item)

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_mockup_product import CatalogMockupProduct
        from ..models.template_mockup_product import TemplateMockupProduct

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:

            def _parse_products_item(data: object) -> Union["CatalogMockupProduct", "TemplateMockupProduct"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    products_item_type_0 = CatalogMockupProduct.from_dict(data)

                    return products_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                products_item_type_1 = TemplateMockupProduct.from_dict(data)

                return products_item_type_1

            products_item = _parse_products_item(products_item_data)

            products.append(products_item)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, MockupTaskCreationFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = MockupTaskCreationFormat(_format_)

        mockup_task_creation = cls(
            products=products,
            format_=format_,
        )

        mockup_task_creation.additional_properties = d
        return mockup_task_creation

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
