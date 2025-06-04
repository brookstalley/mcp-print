from enum import Enum


class MockupTemplatesTemplatePositioning(str, Enum):
    BACKGROUND = "background"
    OVERLAY = "overlay"

    def __str__(self) -> str:
        return str(self.value)
