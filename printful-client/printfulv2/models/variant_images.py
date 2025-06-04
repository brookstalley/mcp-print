from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.variant_image import VariantImage


T = TypeVar("T", bound="VariantImages")


@_attrs_define
class VariantImages:
    """
    Attributes:
        catalog_variant_id (int): Variant ID Example: 4017.
        color (Union[None, str]): Variant color Example: Turquoise.
        primary_hex_color (Union[None, str]): Primary variant hex color used. Use this hex color to fill the mockup.
            Example: #15d0d2.
        secondary_hex_color (Union[None, str]): Secondary variant hex color used. Use this hex color to fill the mockup.
        images (list['VariantImage']): Variant's images
    """

    catalog_variant_id: int
    color: Union[None, str]
    primary_hex_color: Union[None, str]
    secondary_hex_color: Union[None, str]
    images: list["VariantImage"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_variant_id = self.catalog_variant_id

        color: Union[None, str]
        color = self.color

        primary_hex_color: Union[None, str]
        primary_hex_color = self.primary_hex_color

        secondary_hex_color: Union[None, str]
        secondary_hex_color = self.secondary_hex_color

        images = []
        for images_item_data in self.images:
            images_item = images_item_data.to_dict()
            images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_variant_id": catalog_variant_id,
                "color": color,
                "primary_hex_color": primary_hex_color,
                "secondary_hex_color": secondary_hex_color,
                "images": images,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variant_image import VariantImage

        d = dict(src_dict)
        catalog_variant_id = d.pop("catalog_variant_id")

        def _parse_color(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        color = _parse_color(d.pop("color"))

        def _parse_primary_hex_color(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        primary_hex_color = _parse_primary_hex_color(d.pop("primary_hex_color"))

        def _parse_secondary_hex_color(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        secondary_hex_color = _parse_secondary_hex_color(d.pop("secondary_hex_color"))

        images = []
        _images = d.pop("images")
        for images_item_data in _images:
            images_item = VariantImage.from_dict(images_item_data)

            images.append(images_item)

        variant_images = cls(
            catalog_variant_id=catalog_variant_id,
            color=color,
            primary_hex_color=primary_hex_color,
            secondary_hex_color=secondary_hex_color,
            images=images,
        )

        variant_images.additional_properties = d
        return variant_images

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
