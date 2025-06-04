from enum import Enum


class WarehouseItemSummarySource(str, Enum):
    WAREHOUSE = "warehouse"

    def __str__(self) -> str:
        return str(self.value)
