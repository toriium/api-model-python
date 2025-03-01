from datetime import datetime

from src.application.crypt.crypt_service import CryptService
from src.application.user.user_error import UserError
from src.domain.user import UserDomain
from src.data.dtos.users_dto import CreateUserDTO
from src.data.errors.repository_error import RepositoryError
from src.data.repository.users_repository import UsersRepository
from src.presentation.schemas.user_schema import CreateUserInput


class UserService:
    @staticmethod
    def create_user(received_user: CreateUserInput) -> tuple[UserDomain | None, UserError | None]:
        encrypted_password = CryptService.encrypt(value=received_user.password)

        new_user = CreateUserDTO(
            username=received_user.username,
            name=received_user.name,
            password=encrypted_password,
            creation_date=datetime.today()
        )

        result, error = UsersRepository.insert_user(user=new_user)
        if error:
            if error == RepositoryError.duplicate_entry:
                return None, UserError.duplicate_entry

        created_user = UserDomain(**result.dict())
        created_user.password = received_user.password

        return created_user, None

    @staticmethod
    def user_is_valid(username: str, password: str) -> tuple[bool, UserError | None]:
        received_user = UserDomain(username=username, password=password)

        found_user, error = UsersRepository.find_user_by_username(username=received_user.username)
        if error:
            if error == RepositoryError.duplicate_entry:
                return False, None

        if not found_user:
            return False, UserError.user_not_found

        decrypted_password = CryptService.decrypt(found_user.password)
        if decrypted_password == received_user.password:
            return True, None
        else:
            return False, UserError.incorrect_password

    @staticmethod
    def delete_user_by_username(username: str) -> UserError | None:
        error = UsersRepository.delete_user_by_username(username=username)
        if error == RepositoryError.not_found:
            return UserError.not_found
        return None
