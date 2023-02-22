
from src.infrastructure.db_orm.query_obj import delete_obj, insert_obj, select_first_obj
from src.infrastructure.db_orm.tables import TblUsers
from src.infrastructure.dtos.users_dto import CreateUserDTO, UserDTO
from src.infrastructure.errors.sql_error import SQLError


class UsersRepository:
    @staticmethod
    def find_user_by_username(username: str) -> tuple[UserDTO | None, SQLError | None]:
        query_result = select_first_obj(obj_table=TblUsers, filter_by={"username": username})
        if query_result:
            return UserDTO.from_orm(query_result), None
        else:
            return None, None

    @staticmethod
    def insert_user(user: CreateUserDTO) -> tuple[UserDTO | None, SQLError | None]:
        user_obj = TblUsers()
        user_obj.username = user.username
        user_obj.name = user.name
        user_obj.password = user.password
        user_obj.creation_date = user.creation_date

        query_result, error = insert_obj(obj=user_obj)
        if error:
            if error == SQLError.duplicate_entry:
                return None, SQLError.duplicate_entry

        if query_result:
            return UserDTO.from_orm(query_result), None
        else:
            return None, None

    @staticmethod
    def delete_user_by_username(username: str) -> SQLError | None:
        error = delete_obj(obj_table=TblUsers, filter_by={"username": username})
        return error if error else None
