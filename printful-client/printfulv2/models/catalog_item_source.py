from enum import Enum


class CatalogItemSource(str, Enum):
    CATALOG = "catalog"

    def __str__(self) -> str:
        return str(self.value)
