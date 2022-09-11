from enum import Enum


class SQLError(Enum):
    duplicate_entry = "1062 (23000): Duplicate entry"

