from enum import Enum


class MockupTemplatesTemplateType(str, Enum):
    ADVANCED = "advanced"
    COLOR_GROUP = "color_group"
    CUSTOM = "custom"
    NATIVE = "native"

    def __str__(self) -> str:
        return str(self.value)
