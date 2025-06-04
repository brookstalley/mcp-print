from enum import Enum


class GetWarehouseProductsResponse200DataItemWarehouseVariantsItemDimensionsMeasurementSystem(str, Enum):
    IMPERIAL = "imperial"
    METRIC = "metric"

    def __str__(self) -> str:
        return str(self.value)
