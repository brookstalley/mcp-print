import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.catalog_item_summary import CatalogItemSummary
    from ..models.costs import Costs
    from ..models.order_summary_links import OrderSummaryLinks
    from ..models.retail_costs import RetailCosts
    from ..models.warehouse_item_summary import WarehouseItemSummary


T = TypeVar("T", bound="OrderSummary")


@_attrs_define
class OrderSummary:
    """Order summary

    Attributes:
        id (int): Order ID Example: 123.
        external_id (Union[None, str]): Order ID from the external system Example: 4235234213.
        store_id (int): Store ID Example: 10.
        shipping (str): Shipping method. Defaults to 'STANDARD' Example: STANDARD.
        status (str): Order status:<br />
            **draft** - order is not submitted for fulfillment<br />
            **failed** - order was submitted for fulfillment but was not accepted because of an error (problem with address,
            printfiles, charging, etc.)<br />
            **pending** - order has been submitted for fulfillment<br />
            **canceled** - order is canceled<br />
            **onhold** - order has encountered a problem during the fulfillment that needs to be resolved together with the
            Printful customer service<br />
            **inprocess** - order is being fulfilled and is no longer cancellable<br />
            **partial** - order is partially fulfilled (some items are shipped already, the rest will follow)<br />
            **fulfilled** - all items are shipped
             Example: draft.
        created_at (datetime.datetime): Time when the order was created Example: 2023-04-05T06:07:08Z.
        updated_at (datetime.datetime): Time when the order was updated Example: 2023-04-05T06:07:08Z.
        recipient (Address): Information about the address
        costs (Costs): The Order costs (Printful prices)
        retail_costs (RetailCosts): The Order's retail costs
        order_items (list[Union['CatalogItemSummary', 'WarehouseItemSummary']]): Simplified order item list. For a full
            list of all items use the [Get Order Items](#operation/getItemsByOrderId) endpoint.
        field_links (OrderSummaryLinks): HATEOAS links
    """

    id: int
    external_id: Union[None, str]
    store_id: int
    shipping: str
    status: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    recipient: "Address"
    costs: "Costs"
    retail_costs: "RetailCosts"
    order_items: list[Union["CatalogItemSummary", "WarehouseItemSummary"]]
    field_links: "OrderSummaryLinks"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_item_summary import CatalogItemSummary

        id = self.id

        external_id: Union[None, str]
        external_id = self.external_id

        store_id = self.store_id

        shipping = self.shipping

        status = self.status

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        recipient = self.recipient.to_dict()

        costs = self.costs.to_dict()

        retail_costs = self.retail_costs.to_dict()

        order_items = []
        for order_items_item_data in self.order_items:
            order_items_item: dict[str, Any]
            if isinstance(order_items_item_data, CatalogItemSummary):
                order_items_item = order_items_item_data.to_dict()
            else:
                order_items_item = order_items_item_data.to_dict()

            order_items.append(order_items_item)

        field_links = self.field_links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "external_id": external_id,
                "store_id": store_id,
                "shipping": shipping,
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
                "recipient": recipient,
                "costs": costs,
                "retail_costs": retail_costs,
                "order_items": order_items,
                "_links": field_links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.catalog_item_summary import CatalogItemSummary
        from ..models.costs import Costs
        from ..models.order_summary_links import OrderSummaryLinks
        from ..models.retail_costs import RetailCosts
        from ..models.warehouse_item_summary import WarehouseItemSummary

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_external_id(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        external_id = _parse_external_id(d.pop("external_id"))

        store_id = d.pop("store_id")

        shipping = d.pop("shipping")

        status = d.pop("status")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        recipient = Address.from_dict(d.pop("recipient"))

        costs = Costs.from_dict(d.pop("costs"))

        retail_costs = RetailCosts.from_dict(d.pop("retail_costs"))

        order_items = []
        _order_items = d.pop("order_items")
        for order_items_item_data in _order_items:

            def _parse_order_items_item(data: object) -> Union["CatalogItemSummary", "WarehouseItemSummary"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    order_items_item_type_0 = CatalogItemSummary.from_dict(data)

                    return order_items_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                order_items_item_type_1 = WarehouseItemSummary.from_dict(data)

                return order_items_item_type_1

            order_items_item = _parse_order_items_item(order_items_item_data)

            order_items.append(order_items_item)

        field_links = OrderSummaryLinks.from_dict(d.pop("_links"))

        order_summary = cls(
            id=id,
            external_id=external_id,
            store_id=store_id,
            shipping=shipping,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            recipient=recipient,
            costs=costs,
            retail_costs=retail_costs,
            order_items=order_items,
            field_links=field_links,
        )

        order_summary.additional_properties = d
        return order_summary

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
