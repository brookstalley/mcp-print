from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.warehouse_item_summary_source import WarehouseItemSummarySource
from ..models.warehouse_item_summary_type import WarehouseItemSummaryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.warehouse_item_summary_links import WarehouseItemSummaryLinks


T = TypeVar("T", bound="WarehouseItemSummary")


@_attrs_define
class WarehouseItemSummary:
    """Simplified information about the Warehouse Item

    Attributes:
        id (Union[Unset, int]): Item ID Example: 1234.
        type_ (Union[Unset, WarehouseItemSummaryType]): The item type Example: order_item.
        source (Union[Unset, WarehouseItemSummarySource]): Item source Example: warehouse.
        warehouse_product_variant_id (Union[Unset, int]): ID of warehouse product associated with the Item Example:
            1123581321.
        external_id (Union[None, Unset, str]): Item user specified external ID Example: 123_abc.
        quantity (Union[Unset, int]): Item quantity Example: 1.
        name (Union[Unset, str]): Item custom name Example: Custom name.
        price (Union[Unset, str]): The price Printful charges for the Item Example: 8.00.
        retail_price (Union[Unset, str]): Item retail price Example: 10.00.
        currency (Union[Unset, str]): The price currency Example: EUR.
        retail_currency (Union[Unset, str]): The retail price currency Example: USD.
        field_links (Union[Unset, WarehouseItemSummaryLinks]): HATEOAS links
    """

    id: Union[Unset, int] = UNSET
    type_: Union[Unset, WarehouseItemSummaryType] = UNSET
    source: Union[Unset, WarehouseItemSummarySource] = UNSET
    warehouse_product_variant_id: Union[Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    retail_price: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    retail_currency: Union[Unset, str] = UNSET
    field_links: Union[Unset, "WarehouseItemSummaryLinks"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        warehouse_product_variant_id = self.warehouse_product_variant_id

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        quantity = self.quantity

        name = self.name

        price = self.price

        retail_price = self.retail_price

        currency = self.currency

        retail_currency = self.retail_currency

        field_links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_links, Unset):
            field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if source is not UNSET:
            field_dict["source"] = source
        if warehouse_product_variant_id is not UNSET:
            field_dict["warehouse_product_variant_id"] = warehouse_product_variant_id
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if name is not UNSET:
            field_dict["name"] = name
        if price is not UNSET:
            field_dict["price"] = price
        if retail_price is not UNSET:
            field_dict["retail_price"] = retail_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if retail_currency is not UNSET:
            field_dict["retail_currency"] = retail_currency
        if field_links is not UNSET:
            field_dict["_links"] = field_links

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.warehouse_item_summary_links import WarehouseItemSummaryLinks

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, WarehouseItemSummaryType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WarehouseItemSummaryType(_type_)

        _source = d.pop("source", UNSET)
        source: Union[Unset, WarehouseItemSummarySource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = WarehouseItemSummarySource(_source)

        warehouse_product_variant_id = d.pop("warehouse_product_variant_id", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        quantity = d.pop("quantity", UNSET)

        name = d.pop("name", UNSET)

        price = d.pop("price", UNSET)

        retail_price = d.pop("retail_price", UNSET)

        currency = d.pop("currency", UNSET)

        retail_currency = d.pop("retail_currency", UNSET)

        _field_links = d.pop("_links", UNSET)
        field_links: Union[Unset, WarehouseItemSummaryLinks]
        if isinstance(_field_links, Unset):
            field_links = UNSET
        else:
            field_links = WarehouseItemSummaryLinks.from_dict(_field_links)

        warehouse_item_summary = cls(
            id=id,
            type_=type_,
            source=source,
            warehouse_product_variant_id=warehouse_product_variant_id,
            external_id=external_id,
            quantity=quantity,
            name=name,
            price=price,
            retail_price=retail_price,
            currency=currency,
            retail_currency=retail_currency,
            field_links=field_links,
        )

        warehouse_item_summary.additional_properties = d
        return warehouse_item_summary

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
