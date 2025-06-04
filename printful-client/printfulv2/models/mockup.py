from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Mockup")


@_attrs_define
class Mockup:
    """Result of mockup generator tasks.

    Attributes:
        placement (str): Placement name for which the mockup was generated Example: front.
        display_name (str): This is a name that can be displayed to end customers. Example: Front Print.
        technique (str): Technique name for which the mockup was generated Example: dtg.
        style_id (int): Mockup style identifier. Available mockup styles can be found under _[Retrieve catalog product
            mockup styles](#operation/retrieveMockupStylesByProductId)_. Example: 1.
        mockup_url (str): Temporary URL to generated mockup image. Image will be removed from the hosting after a day so
            make sure to persist a copy if needed. Example: https://printful-
            upload.s3-accelerate.amazonaws.com/tmp/9c711aabb422cd386da3cb41735069f3/unisex-staple-t-shirt-white-
            front-659e8b94763bc.png.
    """

    placement: str
    display_name: str
    technique: str
    style_id: int
    mockup_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        placement = self.placement

        display_name = self.display_name

        technique = self.technique

        style_id = self.style_id

        mockup_url = self.mockup_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "placement": placement,
                "display_name": display_name,
                "technique": technique,
                "style_id": style_id,
                "mockup_url": mockup_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        placement = d.pop("placement")

        display_name = d.pop("display_name")

        technique = d.pop("technique")

        style_id = d.pop("style_id")

        mockup_url = d.pop("mockup_url")

        mockup = cls(
            placement=placement,
            display_name=display_name,
            technique=technique,
            style_id=style_id,
            mockup_url=mockup_url,
        )

        mockup.additional_properties = d
        return mockup

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
