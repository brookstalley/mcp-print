from enum import Enum


class LifelikeOptionName(str, Enum):
    LIFELIKE = "lifelike"

    def __str__(self) -> str:
        return str(self.value)
