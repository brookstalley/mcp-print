from enum import Enum


class ThreadColorsOptionName(str, Enum):
    THREAD_COLORS = "thread_colors"

    def __str__(self) -> str:
        return str(self.value)
