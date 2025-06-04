from enum import Enum


class GetWarehouseProductByIdResponse200DataStatus(str, Enum):
    APPROVED = "approved"
    AWAITING_APPROVAL = "awaiting_approval"
    DECLINED = "declined"
    DRAFT = "draft"
    SUSPENDED = "suspended"

    def __str__(self) -> str:
        return str(self.value)
