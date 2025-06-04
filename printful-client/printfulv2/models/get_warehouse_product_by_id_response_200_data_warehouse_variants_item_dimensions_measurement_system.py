from enum import Enum


class GetWarehouseProductByIdResponse200DataWarehouseVariantsItemDimensionsMeasurementSystem(str, Enum):
    IMPERIAL = "imperial"
    METRIC = "metric"

    def __str__(self) -> str:
        return str(self.value)
