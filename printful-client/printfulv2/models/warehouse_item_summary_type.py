from enum import Enum


class WarehouseItemSummaryType(str, Enum):
    BRANDING_ITEM = "branding_item"
    ORDER_ITEM = "order_item"

    def __str__(self) -> str:
        return str(self.value)
