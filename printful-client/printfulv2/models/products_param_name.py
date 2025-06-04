from enum import Enum


class ProductsParamName(str, Enum):
    PRODUCTS = "products"

    def __str__(self) -> str:
        return str(self.value)
