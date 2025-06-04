from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variant_links import VariantLinks


T = TypeVar("T", bound="Variant")


@_attrs_define
class Variant:
    """
    Attributes:
        id (int): Variant ID, use this to specify the product when creating orders Example: 100.
        catalog_product_id (int): ID of the product that this variant belongs to Example: 12.
        name (str): Display name Example: Gildan 64000 Unisex Softstyle T-Shirt with Tear Away (Black / 2XL).
        size (str): Item size Example: 2XL.
        color (Union[None, str]): Item color Example: Black.
        color_code (Union[None, str]): Hexadecimal RGB color code. May not exactly reflect the real-world color Example:
            #14191e.
        color_code2 (Union[None, str]): Secondary hexadecimal RGB color code. May not exactly reflect the real-world
            color
        image (str): URL of a preview image for this variant Example:
            https://files.cdn.printful.com/products/12/629_1517916489.jpg.
        field_links (VariantLinks): HATEOAS links
        placement_dimensions (Union[Unset, Any]): A list of placement configuration objects, each specifying the layout
            details for a particular placement.
    """

    id: int
    catalog_product_id: int
    name: str
    size: str
    color: Union[None, str]
    color_code: Union[None, str]
    color_code2: Union[None, str]
    image: str
    field_links: "VariantLinks"
    placement_dimensions: Union[Unset, Any] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        catalog_product_id = self.catalog_product_id

        name = self.name

        size = self.size

        color: Union[None, str]
        color = self.color

        color_code: Union[None, str]
        color_code = self.color_code

        color_code2: Union[None, str]
        color_code2 = self.color_code2

        image = self.image

        field_links = self.field_links.to_dict()

        placement_dimensions = self.placement_dimensions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "catalog_product_id": catalog_product_id,
                "name": name,
                "size": size,
                "color": color,
                "color_code": color_code,
                "color_code2": color_code2,
                "image": image,
                "_links": field_links,
            }
        )
        if placement_dimensions is not UNSET:
            field_dict["placement_dimensions"] = placement_dimensions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_links import VariantLinks

        d = dict(src_dict)
        id = d.pop("id")

        catalog_product_id = d.pop("catalog_product_id")

        name = d.pop("name")

        size = d.pop("size")

        def _parse_color(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        color = _parse_color(d.pop("color"))

        def _parse_color_code(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        color_code = _parse_color_code(d.pop("color_code"))

        def _parse_color_code2(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        color_code2 = _parse_color_code2(d.pop("color_code2"))

        image = d.pop("image")

        field_links = VariantLinks.from_dict(d.pop("_links"))

        placement_dimensions = d.pop("placement_dimensions", UNSET)

        variant = cls(
            id=id,
            catalog_product_id=catalog_product_id,
            name=name,
            size=size,
            color=color,
            color_code=color_code,
            color_code2=color_code2,
            image=image,
            field_links=field_links,
            placement_dimensions=placement_dimensions,
        )

        variant.additional_properties = d
        return variant

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
