from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VariantImage")


@_attrs_define
class VariantImage:
    """
    Attributes:
        placement (str): Placement associated with the image Example: front.
        image_url (Union[None, str]): image URL Example: https://printful-mockups-
            dev.s3.amazonaws.com/239-nl4600/medium/flat/front/05_nl4600_flat_front_base_whitebg.png?v=1666248709.
        background_color (str): Background color of an image. Null if background transparent Example: #0f0f0f.
        background_image (Union[None, str]): Background image of an image specified in the `image_url`. Null if no
            background image Example: https://printful-mockups-
            dev.s3.amazonaws.com/239-nl4600/medium/flat/front/05_nl4600_flat_front_base_whitebg.png?v=1666248709.
    """

    placement: str
    image_url: Union[None, str]
    background_color: str
    background_image: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        placement = self.placement

        image_url: Union[None, str]
        image_url = self.image_url

        background_color = self.background_color

        background_image: Union[None, str]
        background_image = self.background_image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placement": placement,
                "image_url": image_url,
                "background_color": background_color,
                "background_image": background_image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        placement = d.pop("placement")

        def _parse_image_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        image_url = _parse_image_url(d.pop("image_url"))

        background_color = d.pop("background_color")

        def _parse_background_image(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        background_image = _parse_background_image(d.pop("background_image"))

        variant_image = cls(
            placement=placement,
            image_url=image_url,
            background_color=background_color,
            background_image=background_image,
        )

        variant_image.additional_properties = d
        return variant_image

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
