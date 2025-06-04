from enum import Enum


class MockupTemplatesOrientation(str, Enum):
    ANY = "any"
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def __str__(self) -> str:
        return str(self.value)
