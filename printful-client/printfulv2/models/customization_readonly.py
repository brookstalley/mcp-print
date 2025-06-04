from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.gift import Gift
    from ..models.packing_slip_readonly import PackingSlipReadonly


T = TypeVar("T", bound="CustomizationReadonly")


@_attrs_define
class CustomizationReadonly:
    """The Order's customization values

    Attributes:
        gift (Gift): The gift subject and message
        packing_slip (PackingSlipReadonly): The values for customized packing slip
    """

    gift: "Gift"
    packing_slip: "PackingSlipReadonly"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift = self.gift.to_dict()

        packing_slip = self.packing_slip.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gift": gift,
                "packing_slip": packing_slip,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift import Gift
        from ..models.packing_slip_readonly import PackingSlipReadonly

        d = dict(src_dict)
        gift = Gift.from_dict(d.pop("gift"))

        packing_slip = PackingSlipReadonly.from_dict(d.pop("packing_slip"))

        customization_readonly = cls(
            gift=gift,
            packing_slip=packing_slip,
        )

        customization_readonly.additional_properties = d
        return customization_readonly

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
