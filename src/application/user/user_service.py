from datetime import date
from typing import Union

from src.application.user.user_error import UserError
from src.domain.user import User
from src.infrastructure.dtos.tbl_users_dto import CreateUserDTO
from src.infrastructure.repository.users_repository import UsersRepository
from src.infrastructure.errors.sql_error import SQLError
from src.presentation.schemas.user_schema import POSTUserInput


class UserService:
    @staticmethod
    def create_user(received_user: POSTUserInput) -> tuple[Union[User, None], Union[UserError, None]]:
        new_user = CreateUserDTO(
            username=received_user.username,
            name=received_user.name,
            password=received_user.password,
            creation_date=date.today()
        )

        result, error = UsersRepository.insert_user(user=new_user)
        if error:
            if error == SQLError.duplicate_entry:
                return None, UserError.duplicate_entry

        return User(**result.dict()), None

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
