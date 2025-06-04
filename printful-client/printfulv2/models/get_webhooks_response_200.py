from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_info import WebhookInfo


T = TypeVar("T", bound="GetWebhooksResponse200")


@_attrs_define
class GetWebhooksResponse200:
    """
    Attributes:
        code (Union[Unset, int]): Response status code `200` Example: 200.
        result (Union[Unset, WebhookInfo]):
    """

    code: Union[Unset, int] = UNSET
    result: Union[Unset, "WebhookInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_info import WebhookInfo

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _result = d.pop("result", UNSET)
        result: Union[Unset, WebhookInfo]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = WebhookInfo.from_dict(_result)

        get_webhooks_response_200 = cls(
            code=code,
            result=result,
        )

        get_webhooks_response_200.additional_properties = d
        return get_webhooks_response_200

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
