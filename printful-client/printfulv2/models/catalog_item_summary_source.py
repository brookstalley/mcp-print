from enum import Enum


class CatalogItemSummarySource(str, Enum):
    CATALOG = "catalog"

    def __str__(self) -> str:
        return str(self.value)
