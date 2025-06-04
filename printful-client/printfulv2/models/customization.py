from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift import Gift
    from ..models.packing_slip import PackingSlip


T = TypeVar("T", bound="Customization")


@_attrs_define
class Customization:
    """The Order's customization values

    Attributes:
        gift (Union[Unset, Gift]): The gift subject and message
        packing_slip (Union[Unset, PackingSlip]): The values for customized packing slip
    """

    gift: Union[Unset, "Gift"] = UNSET
    packing_slip: Union[Unset, "PackingSlip"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gift: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.gift, Unset):
            gift = self.gift.to_dict()

        packing_slip: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.packing_slip, Unset):
            packing_slip = self.packing_slip.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gift is not UNSET:
            field_dict["gift"] = gift
        if packing_slip is not UNSET:
            field_dict["packing_slip"] = packing_slip

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift import Gift
        from ..models.packing_slip import PackingSlip

        d = dict(src_dict)
        _gift = d.pop("gift", UNSET)
        gift: Union[Unset, Gift]
        if isinstance(_gift, Unset):
            gift = UNSET
        else:
            gift = Gift.from_dict(_gift)

        _packing_slip = d.pop("packing_slip", UNSET)
        packing_slip: Union[Unset, PackingSlip]
        if isinstance(_packing_slip, Unset):
            packing_slip = UNSET
        else:
            packing_slip = PackingSlip.from_dict(_packing_slip)

        customization = cls(
            gift=gift,
            packing_slip=packing_slip,
        )

        customization.additional_properties = d
        return customization

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
