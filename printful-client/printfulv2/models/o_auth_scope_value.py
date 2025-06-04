from enum import Enum


class OAuthScopeValue(str, Enum):
    FILE_LIBRARY = "file_library"
    FILE_LIBRARYREAD = "file_library/read"
    ORDERS = "orders"
    ORDERSREAD = "orders/read"
    SYNC_PRODUCTS = "sync_products"
    SYNC_PRODUCTSREAD = "sync_products/read"
    WEBHOOKSREAD = "webhooks/read"

    def __str__(self) -> str:
        return str(self.value)
