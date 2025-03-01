
from src.data.db_orm.query_obj import delete_obj, insert_obj, select_first_obj
from src.data.db_orm.tables import TblUsers
from src.data.dtos.users_dto import UserDTO
from src.data.errors.repository_error import RepositoryError
from src.data.errors.sql_error import SQLError
from src.domain.user import UserDomain


class UsersRepository:
    @staticmethod
    def find_user_by_username(username: str) -> tuple[UserDTO | None, RepositoryError | None]:
        query_result = select_first_obj(obj_table=TblUsers,  where_clauses=[TblUsers.username==username])
        if query_result:
            return UserDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def insert_user(user: UserDomain) -> tuple[UserDTO | None, RepositoryError | None]:
        user_obj = TblUsers()
        user_obj.username = user.username
        user_obj.name = user.name
        user_obj.password = user.password
        user_obj.creation_date = user.creation_date

        query_result, error = insert_obj(obj=user_obj)
        if error:
            if error == SQLError.duplicate_entry:
                return None, RepositoryError.duplicate_entry

        if query_result:
            return UserDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def delete_user_by_username(username: str) -> RepositoryError | None:
        error = delete_obj(obj_table=TblUsers,where_clauses=[TblUsers.username==username])
        return error if error else None
