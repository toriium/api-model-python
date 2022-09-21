from typing import Union, Tuple

from src.infrastructure.dtos.tbl_users_dto import TblUsersDTO
from src.infrastructure.db_orm.tables.tbl_users import TblUsers
from src.infrastructure.errors.sql_error import SQLError
from src.infrastructure.db_orm.query_obj import select_first_obj, select_all_obj, insert_obj


class UsersRepository:
    @staticmethod
    def find_user_by_username(username: str) -> tuple[Union[TblUsersDTO, None], Union[SQLError, None]]:
        query_result = select_first_obj(obj_table=TblUsers, kw_filters={"username": username})
        if query_result:
            return TblUsersDTO.from_orm(query_result), None
        else:
            return None, None
