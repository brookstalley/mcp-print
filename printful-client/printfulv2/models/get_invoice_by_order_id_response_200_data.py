from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_invoice_by_order_id_response_200_data_links import GetInvoiceByOrderIdResponse200DataLinks


T = TypeVar("T", bound="GetInvoiceByOrderIdResponse200Data")


@_attrs_define
class GetInvoiceByOrderIdResponse200Data:
    """
    Attributes:
        media_type (str): This property is used to describe the media type of the encoded base64 value. It is necessary
            to use this property when decoding the content property. Example: application/pdf.
        content (str): The base64 encoded document containing the invoice. Example:
            0xLjQKJeLjz9MKMyAwIG9iago8PC9UeXBlIC9QYWdlCi9QYXJlbnQgMSAwIFIKL01lZG.
        field_links (GetInvoiceByOrderIdResponse200DataLinks): HATEOAS links
    """

    media_type: str
    content: str
    field_links: "GetInvoiceByOrderIdResponse200DataLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_type = self.media_type

        content = self.content

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media_type": media_type,
                "content": content,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_invoice_by_order_id_response_200_data_links import GetInvoiceByOrderIdResponse200DataLinks

        d = dict(src_dict)
        media_type = d.pop("media_type")

        content = d.pop("content")

        field_links = GetInvoiceByOrderIdResponse200DataLinks.from_dict(d.pop("_links"))

        get_invoice_by_order_id_response_200_data = cls(
            media_type=media_type,
            content=content,
            field_links=field_links,
        )

        get_invoice_by_order_id_response_200_data.additional_properties = d
        return get_invoice_by_order_id_response_200_data

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
