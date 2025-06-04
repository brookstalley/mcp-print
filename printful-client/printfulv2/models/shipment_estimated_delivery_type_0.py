import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShipmentEstimatedDeliveryType0")


@_attrs_define
class ShipmentEstimatedDeliveryType0:
    """
    Attributes:
        from_date (Union[Unset, datetime.date]): Earliest estimated date the shipment will arrive Example: 2023-06-15.
        to_date (Union[Unset, datetime.date]): Latest estimated date the shipment will arrive Example: 2023-06-15.
        calculated_at (Union[Unset, datetime.datetime]):  Example: 2023-06-15T16:35:35Z.
    """

    from_date: Union[Unset, datetime.date] = UNSET
    to_date: Union[Unset, datetime.date] = UNSET
    calculated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_date: Union[Unset, str] = UNSET
        if not isinstance(self.from_date, Unset):
            from_date = self.from_date.isoformat()

        to_date: Union[Unset, str] = UNSET
        if not isinstance(self.to_date, Unset):
            to_date = self.to_date.isoformat()

        calculated_at: Union[Unset, str] = UNSET
        if not isinstance(self.calculated_at, Unset):
            calculated_at = self.calculated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_date is not UNSET:
            field_dict["from_date"] = from_date
        if to_date is not UNSET:
            field_dict["to_date"] = to_date
        if calculated_at is not UNSET:
            field_dict["calculated_at"] = calculated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _from_date = d.pop("from_date", UNSET)
        from_date: Union[Unset, datetime.date]
        if isinstance(_from_date, Unset):
            from_date = UNSET
        else:
            from_date = isoparse(_from_date).date()

        _to_date = d.pop("to_date", UNSET)
        to_date: Union[Unset, datetime.date]
        if isinstance(_to_date, Unset):
            to_date = UNSET
        else:
            to_date = isoparse(_to_date).date()

        _calculated_at = d.pop("calculated_at", UNSET)
        calculated_at: Union[Unset, datetime.datetime]
        if isinstance(_calculated_at, Unset):
            calculated_at = UNSET
        else:
            calculated_at = isoparse(_calculated_at)

        shipment_estimated_delivery_type_0 = cls(
            from_date=from_date,
            to_date=to_date,
            calculated_at=calculated_at,
        )

        shipment_estimated_delivery_type_0.additional_properties = d
        return shipment_estimated_delivery_type_0

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
