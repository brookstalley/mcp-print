from enum import Enum


class OAuthScopeName(str, Enum):
    VIEW_AND_MANAGE_ORDERS_OF_THE_AUTHORIZED_STORE = "View and manage orders of the authorized store"
    VIEW_AND_MANAGE_STORE_FILES = "View and manage store files"
    VIEW_AND_MANAGE_STORE_PRODUCTS = "View and manage store products"
    VIEW_AND_MANAGE_STORE_WEBHOOKS = "View and manage store webhooks"
    VIEW_ORDERS_OF_THE_AUTHORIZED_STORE = "View orders of the authorized store"
    VIEW_STORE_FILES = "View store files"
    VIEW_STORE_PRODUCTS = "View store products"
    VIEW_STORE_WEBHOOKS = "View store webhooks"

    def __str__(self) -> str:
        return str(self.value)
