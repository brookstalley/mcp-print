from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.catalog_item_summary_source import CatalogItemSummarySource
from ..models.catalog_item_summary_type import CatalogItemSummaryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_item_summary_links import CatalogItemSummaryLinks


T = TypeVar("T", bound="CatalogItemSummary")


@_attrs_define
class CatalogItemSummary:
    """Simplified information about the Catalog Item

    Attributes:
        id (int): Item ID Example: 1234.
        type_ (CatalogItemSummaryType): The item type Example: order_item.
        source (CatalogItemSummarySource): Item source Example: catalog.
        catalog_variant_id (int): Catalog Variant ID associated with the Item Example: 4011.
        external_id (Union[None, str]): Item user specified external ID Example: 123_abc.
        quantity (int): Item quantity Example: 1.
        price (str): The price Printful charges for the Item Example: 8.00.
        retail_price (str): Item retail price Example: 10.00.
        currency (str): The price currency Example: EUR.
        retail_currency (str): The retail price currency Example: USD.
        field_links (CatalogItemSummaryLinks): HATEOAS links
        name (Union[Unset, str]): Item custom name Example: Custom name.
    """

    id: int
    type_: CatalogItemSummaryType
    source: CatalogItemSummarySource
    catalog_variant_id: int
    external_id: Union[None, str]
    quantity: int
    price: str
    retail_price: str
    currency: str
    retail_currency: str
    field_links: "CatalogItemSummaryLinks"
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        source = self.source.value

        catalog_variant_id = self.catalog_variant_id

        external_id: Union[None, str]
        external_id = self.external_id

        quantity = self.quantity

        price = self.price

        retail_price = self.retail_price

        currency = self.currency

        retail_currency = self.retail_currency

        field_links = self.field_links.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "source": source,
                "catalog_variant_id": catalog_variant_id,
                "external_id": external_id,
                "quantity": quantity,
                "price": price,
                "retail_price": retail_price,
                "currency": currency,
                "retail_currency": retail_currency,
                "_links": field_links,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_item_summary_links import CatalogItemSummaryLinks

        d = dict(src_dict)
        id = d.pop("id")

        type_ = CatalogItemSummaryType(d.pop("type"))

        source = CatalogItemSummarySource(d.pop("source"))

        catalog_variant_id = d.pop("catalog_variant_id")

        def _parse_external_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_id = _parse_external_id(d.pop("external_id"))

        quantity = d.pop("quantity")

        price = d.pop("price")

        retail_price = d.pop("retail_price")

        currency = d.pop("currency")

        retail_currency = d.pop("retail_currency")

        field_links = CatalogItemSummaryLinks.from_dict(d.pop("_links"))

        name = d.pop("name", UNSET)

        catalog_item_summary = cls(
            id=id,
            type_=type_,
            source=source,
            catalog_variant_id=catalog_variant_id,
            external_id=external_id,
            quantity=quantity,
            price=price,
            retail_price=retail_price,
            currency=currency,
            retail_currency=retail_currency,
            field_links=field_links,
            name=name,
        )

        catalog_item_summary.additional_properties = d
        return catalog_item_summary

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
