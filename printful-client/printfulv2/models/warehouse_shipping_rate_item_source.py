from enum import Enum


class WarehouseShippingRateItemSource(str, Enum):
    CATALOG = "catalog"

    def __str__(self) -> str:
        return str(self.value)
