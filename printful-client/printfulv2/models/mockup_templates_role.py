from enum import Enum


class MockupTemplatesRole(str, Enum):
    ADVANCED_TEMPLATE = "advanced_template"
    EXTRA = "extra"
    PRIMARY = "primary"
    TEMPLATE = "template"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
