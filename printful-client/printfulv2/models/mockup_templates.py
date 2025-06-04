from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mockup_templates_orientation import MockupTemplatesOrientation
from ..models.mockup_templates_role import MockupTemplatesRole
from ..models.mockup_templates_template_positioning import MockupTemplatesTemplatePositioning
from ..models.mockup_templates_template_type import MockupTemplatesTemplateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MockupTemplates")


@_attrs_define
class MockupTemplates:
    """Data containing information about the available mockup templates which can be used for user-side positioning. For
    example for intention of generating mockups without the use of Printful's mockup generator.

        Attributes:
            catalog_variant_ids (list[int]): A list of variant IDs for which the positions apply.
            placement (str): Catalog product placement that is used for the design. Example: front.
            technique (str): Catalog product technique that is used for the design. Example: dtg.
            image_url (str): Semi-transparent main template image URL. Example:
                https://www.printful.com/files/generator/40/11oz_template.png.
            background_url (Union[None, str]): Background image URL (optional). Used for certain mockups e.g. a wall behind
                hanged poster. If it's defined it is intended to be layered under the image defined in `image_url`.
            background_color (Union[None, int]): HEX color code that should be used as a background color of `image_url`.
            template_width (int): Width of the whole template in pixels. Example: 560.
            template_height (int): Height of the whole template in pixels. Example: 295.
            print_area_width (int): Print area width (image is positioned in this area). Example: 520.
            print_area_height (int): Print area height (image is positioned in this area). Example: 202.
            print_area_top (int): Print area top offset (offset in template). Example: 18.
            print_area_left (int): Print area left offset (offset in template). Example: 20.
            template_positioning (MockupTemplatesTemplatePositioning): Should the main template image (image_url) be used as
                an overlay or as a background. Example: overlay.
            orientation (MockupTemplatesOrientation): Wall art product orientation. Possible values: horizontal, vertical,
                any Example: any.
            template_type (Union[Unset, MockupTemplatesTemplateType]): Type of inside label used, "native" refers to labels
                that have preset information, "custom" are fully customizable and require the user to supply country of
                manufacturing origin, original garment size, and material information. "advanced" is for products like for
                products like AOP Tote. "color_group" for the new inside labels where there are multiple designs for the
                overlay.
            role (Union[Unset, MockupTemplatesRole]): Mockup template role. Example: template.
    """

    catalog_variant_ids: list[int]
    placement: str
    technique: str
    image_url: str
    background_url: Union[None, str]
    background_color: Union[None, int]
    template_width: int
    template_height: int
    print_area_width: int
    print_area_height: int
    print_area_top: int
    print_area_left: int
    template_positioning: MockupTemplatesTemplatePositioning
    orientation: MockupTemplatesOrientation
    template_type: Union[Unset, MockupTemplatesTemplateType] = UNSET
    role: Union[Unset, MockupTemplatesRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        catalog_variant_ids = self.catalog_variant_ids

        placement = self.placement

        technique = self.technique

        image_url = self.image_url

        background_url: Union[None, str]
        background_url = self.background_url

        background_color: Union[None, int]
        background_color = self.background_color

        template_width = self.template_width

        template_height = self.template_height

        print_area_width = self.print_area_width

        print_area_height = self.print_area_height

        print_area_top = self.print_area_top

        print_area_left = self.print_area_left

        template_positioning = self.template_positioning.value

        orientation = self.orientation.value

        template_type: Union[Unset, str] = UNSET
        if not isinstance(self.template_type, Unset):
            template_type = self.template_type.value

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_variant_ids": catalog_variant_ids,
                "placement": placement,
                "technique": technique,
                "image_url": image_url,
                "background_url": background_url,
                "background_color": background_color,
                "template_width": template_width,
                "template_height": template_height,
                "print_area_width": print_area_width,
                "print_area_height": print_area_height,
                "print_area_top": print_area_top,
                "print_area_left": print_area_left,
                "template_positioning": template_positioning,
                "orientation": orientation,
            }
        )
        if template_type is not UNSET:
            field_dict["template_type"] = template_type
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        catalog_variant_ids = cast(list[int], d.pop("catalog_variant_ids"))

        placement = d.pop("placement")

        technique = d.pop("technique")

        image_url = d.pop("image_url")

        def _parse_background_url(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        background_url = _parse_background_url(d.pop("background_url"))

        def _parse_background_color(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        background_color = _parse_background_color(d.pop("background_color"))

        template_width = d.pop("template_width")

        template_height = d.pop("template_height")

        print_area_width = d.pop("print_area_width")

        print_area_height = d.pop("print_area_height")

        print_area_top = d.pop("print_area_top")

        print_area_left = d.pop("print_area_left")

        template_positioning = MockupTemplatesTemplatePositioning(d.pop("template_positioning"))

        orientation = MockupTemplatesOrientation(d.pop("orientation"))

        _template_type = d.pop("template_type", UNSET)
        template_type: Union[Unset, MockupTemplatesTemplateType]
        if isinstance(_template_type, Unset):
            template_type = UNSET
        else:
            template_type = MockupTemplatesTemplateType(_template_type)

        _role = d.pop("role", UNSET)
        role: Union[Unset, MockupTemplatesRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = MockupTemplatesRole(_role)

        mockup_templates = cls(
            catalog_variant_ids=catalog_variant_ids,
            placement=placement,
            technique=technique,
            image_url=image_url,
            background_url=background_url,
            background_color=background_color,
            template_width=template_width,
            template_height=template_height,
            print_area_width=print_area_width,
            print_area_height=print_area_height,
            print_area_top=print_area_top,
            print_area_left=print_area_left,
            template_positioning=template_positioning,
            orientation=orientation,
            template_type=template_type,
            role=role,
        )

        mockup_templates.additional_properties = d
        return mockup_templates

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
