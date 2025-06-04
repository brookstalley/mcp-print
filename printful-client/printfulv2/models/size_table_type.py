from enum import Enum


class SizeTableType(str, Enum):
    INTERNATIONAL = "international"
    MEASURE_YOURSELF = "measure_yourself"
    PRODUCT_MEASURE = "product_measure"

    def __str__(self) -> str:
        return str(self.value)
