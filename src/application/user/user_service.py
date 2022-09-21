from typing import Union

from src.application.user.user_error import UserError
from src.domain.user import User
from src.infrastructure.repository.users_repository import UsersRepository
from src.infrastructure.errors.sql_error import SQLError


class UserService:
    # @staticmethod
    # def create_user(username: str, password: str) -> tuple[bool, Union[UserError, None]]:
    #     received_user = User(username=username, password=password)

    @staticmethod
    def user_is_valid(username: str, password: str) -> tuple[bool, Union[UserError, None]]:
        received_user = User(username=username, password=password)

        found_user, error = UsersRepository.find_user_by_username(username=received_user.username)
        if error:
            if error == SQLError.duplicate_entry:
                return False, None

        if not found_user:
            return False, None

        if found_user.password == received_user.password:
            return True, None
