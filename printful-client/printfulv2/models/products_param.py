from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.products_param_name import ProductsParamName
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_data import ProductData


T = TypeVar("T", bound="ProductsParam")


@_attrs_define
class ProductsParam:
    """
    Attributes:
        name (Union[Unset, ProductsParamName]): Param name. Example: products.
        value (Union[Unset, list['ProductData']]): Param value - list of product data. Example: [{'id': 1}, {'id': 71}].
    """

    name: Union[Unset, ProductsParamName] = UNSET
    value: Union[Unset, list["ProductData"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name: Union[Unset, str] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name.value

        value: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.value, Unset):
            value = []
            for value_item_data in self.value:
                value_item = value_item_data.to_dict()
                value.append(value_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_data import ProductData

        d = dict(src_dict)
        _name = d.pop("name", UNSET)
        name: Union[Unset, ProductsParamName]
        if isinstance(_name, Unset):
            name = UNSET
        else:
            name = ProductsParamName(_name)

        value = []
        _value = d.pop("value", UNSET)
        for value_item_data in _value or []:
            value_item = ProductData.from_dict(value_item_data)

            value.append(value_item)

        products_param = cls(
            name=name,
            value=value,
        )

        products_param.additional_properties = d
        return products_param

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
