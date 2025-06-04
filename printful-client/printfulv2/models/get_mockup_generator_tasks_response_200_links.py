from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.hateoas_link import HateoasLink


T = TypeVar("T", bound="GetMockupGeneratorTasksResponse200Links")


@_attrs_define
class GetMockupGeneratorTasksResponse200Links:
    """HATEOAS links

    Attributes:
        self_ (HateoasLink):
        next_ (Union[Unset, HateoasLink]):
        previous (Union[Unset, HateoasLink]):
        first (Union[Unset, HateoasLink]):
        last (Union[Unset, HateoasLink]):
    """

    self_: "HateoasLink"
    next_: Union[Unset, "HateoasLink"] = UNSET
    previous: Union[Unset, "HateoasLink"] = UNSET
    first: Union[Unset, "HateoasLink"] = UNSET
    last: Union[Unset, "HateoasLink"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_.to_dict()

        next_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.next_, Unset):
            next_ = self.next_.to_dict()

        previous: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        first: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.first, Unset):
            first = self.first.to_dict()

        last: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last, Unset):
            last = self.last.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "self": self_,
            }
        )
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hateoas_link import HateoasLink

        d = dict(src_dict)
        self_ = HateoasLink.from_dict(d.pop("self"))

        _next_ = d.pop("next", UNSET)
        next_: Union[Unset, HateoasLink]
        if isinstance(_next_, Unset):
            next_ = UNSET
        else:
            next_ = HateoasLink.from_dict(_next_)

        _previous = d.pop("previous", UNSET)
        previous: Union[Unset, HateoasLink]
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = HateoasLink.from_dict(_previous)

        _first = d.pop("first", UNSET)
        first: Union[Unset, HateoasLink]
        if isinstance(_first, Unset):
            first = UNSET
        else:
            first = HateoasLink.from_dict(_first)

        _last = d.pop("last", UNSET)
        last: Union[Unset, HateoasLink]
        if isinstance(_last, Unset):
            last = UNSET
        else:
            last = HateoasLink.from_dict(_last)

        get_mockup_generator_tasks_response_200_links = cls(
            self_=self_,
            next_=next_,
            previous=previous,
            first=first,
            last=last,
        )

        get_mockup_generator_tasks_response_200_links.additional_properties = d
        return get_mockup_generator_tasks_response_200_links

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
