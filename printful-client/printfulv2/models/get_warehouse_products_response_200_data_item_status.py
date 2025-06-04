from enum import Enum


class GetWarehouseProductsResponse200DataItemStatus(str, Enum):
    APPROVED = "approved"
    AWAITING_APPROVAL = "awaiting_approval"
    DECLINED = "declined"
    DRAFT = "draft"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
