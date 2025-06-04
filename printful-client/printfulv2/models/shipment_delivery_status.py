from enum import Enum


class ShipmentDeliveryStatus(str, Enum):
    AVAILABLE_FOR_PICKUP = "available_for_pickup"
    CANCELED = "canceled"
    DELIVERED = "delivered"
    FAILURE = "failure"
    IN_TRANSIT = "in_transit"
    OUT_FOR_DELIVERY = "out_for_delivery"
    PRE_TRANSIT = "pre_transit"
    RETURN_TO_SENDER = "return_to_sender"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
