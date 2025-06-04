from enum import Enum


class ShipmentShipmentStatus(str, Enum):
    CANCELED = "canceled"
    ONHOLD = "onhold"
    OUTSTOCK = "outstock"
    PACKAGED = "packaged"
    PENDING = "pending"
    RETURNED = "returned"
    SHIPPED = "shipped"

    def __str__(self) -> str:
        return str(self.value)
