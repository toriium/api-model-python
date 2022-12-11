from enum import Enum, auto


class UserError(Enum):
    duplicate_entry = auto()
    user_not_found = auto()
    incorrect_password = auto()
    not_found = auto()
