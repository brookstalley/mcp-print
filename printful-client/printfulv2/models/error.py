from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.header_source import HeaderSource
    from ..models.parameter_source import ParameterSource
    from ..models.pointer_source import PointerSource


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """
    Attributes:
        type_ (Union[Unset, str]): a URI that uniquely identifies the validation rule that failed. If it’s a URL, it
            should point to an explanation of the constraint in the documentation. Example:
            https://developers.printful.com/docs/v2/errors#specific-validation-error.
        detail (Union[Unset, str]): A human-readable explanation of the error Example: Parameter `xyz` was incorrect.
        source (Union['HeaderSource', 'ParameterSource', 'PointerSource', Unset]): Source of the value that caused the
            issue
        valid_values (Union[Unset, list[str]]): List of valid values that could be used instead to avoid the error
    """

    type_: Union[Unset, str] = UNSET
    detail: Union[Unset, str] = UNSET
    source: Union["HeaderSource", "ParameterSource", "PointerSource", Unset] = UNSET
    valid_values: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.header_source import HeaderSource
        from ..models.parameter_source import ParameterSource

        type_ = self.type_

        detail = self.detail

        source: Union[Unset, dict[str, Any]]
        if isinstance(self.source, Unset):
            source = UNSET
        elif isinstance(self.source, HeaderSource):
            source = self.source.to_dict()
        elif isinstance(self.source, ParameterSource):
            source = self.source.to_dict()
        else:
            source = self.source.to_dict()

        valid_values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.valid_values, Unset):
            valid_values = self.valid_values

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if detail is not UNSET:
            field_dict["detail"] = detail
        if source is not UNSET:
            field_dict["source"] = source
        if valid_values is not UNSET:
            field_dict["valid_values"] = valid_values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.header_source import HeaderSource
        from ..models.parameter_source import ParameterSource
        from ..models.pointer_source import PointerSource

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        detail = d.pop("detail", UNSET)

        def _parse_source(data: object) -> Union["HeaderSource", "ParameterSource", "PointerSource", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = HeaderSource.from_dict(data)

                return source_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_1 = ParameterSource.from_dict(data)

                return source_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            source_type_2 = PointerSource.from_dict(data)

            return source_type_2

        source = _parse_source(d.pop("source", UNSET))

        valid_values = cast(list[str], d.pop("valid_values", UNSET))

        error = cls(
            type_=type_,
            detail=detail,
            source=source,
            valid_values=valid_values,
        )

        error.additional_properties = d
        return error

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
