from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notes_option_name import NotesOptionName

T = TypeVar("T", bound="NotesOption")


@_attrs_define
class NotesOption:
    """Include additional notes for fulfillment for embroidery prints

    Attributes:
        name (NotesOptionName): Option identifier Example: notes.
        value (str): Additional notes for fulfillment for embroidery prints. Example: Please make sure that top side of
            the print is within print area.
    """

    name: NotesOptionName
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name.value

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = NotesOptionName(d.pop("name"))

        value = d.pop("value")

        notes_option = cls(
            name=name,
            value=value,
        )

        notes_option.additional_properties = d
        return notes_option

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
