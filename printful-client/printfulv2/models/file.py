from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_role import FileRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="File")


@_attrs_define
class File:
    """Information about the added File

    Attributes:
        url (str): Source URL where the file is to be downloaded from. The use of .ai, .psd, and .tiff files has been
            deprecated, if your application uses these file types or accepts these types from users you will need to add
            validation. Example: ​https://www.example.com/files/tshirts/example.png.
        role (Union[Unset, FileRole]): Role of the file Default: FileRole.PRINTFILE. Example: printfile.
        filename (Union[Unset, str]): If the filename is not provided, and something looking like a filename is present
            in the URL (e.g. "something.jpg"), it will be used.
            Otherwise, it will default to `{file_id}.{file_extension}`, with file extension determined based on the media
            type of the file.
             Example: shirt1.png.
        visible (Union[Unset, bool]): Show file in the Printfile Library Default: True. Example: True.
    """

    url: str
    role: Union[Unset, FileRole] = FileRole.PRINTFILE
    filename: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        filename = self.filename

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if role is not UNSET:
            field_dict["role"] = role
        if filename is not UNSET:
            field_dict["filename"] = filename
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        _role = d.pop("role", UNSET)
        role: Union[Unset, FileRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = FileRole(_role)

        filename = d.pop("filename", UNSET)

        visible = d.pop("visible", UNSET)

        file = cls(
            url=url,
            role=role,
            filename=filename,
            visible=visible,
        )

        file.additional_properties = d
        return file

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
