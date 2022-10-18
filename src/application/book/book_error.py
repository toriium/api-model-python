from enum import Enum, auto


class BookError(Enum):
    duplicate_entry = auto()
    not_found = auto()
