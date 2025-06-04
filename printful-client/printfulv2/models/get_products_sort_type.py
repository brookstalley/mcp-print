from enum import Enum


class GetProductsSortType(str, Enum):
    BESTSELLER = "bestseller"
    NEW = "new"
    PRICE = "price"
    RATING = "rating"

    def __str__(self) -> str:
        return str(self.value)
