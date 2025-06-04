from enum import Enum


class SellingRegionStockAvailabilityAvailability(str, Enum):
    IN_STOCK = "in stock"
    NOT_FULFILLABLE = "not fulfillable"
    OUT_OF_STOCK = "out of stock"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
