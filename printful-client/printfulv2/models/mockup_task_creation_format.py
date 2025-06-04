from enum import Enum


class MockupTaskCreationFormat(str, Enum):
    JPG = "jpg"
    PNG = "png"

    def __str__(self) -> str:
        return str(self.value)
