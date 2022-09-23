from src.infrastructure.db_orm.query_obj import insert_obj
from src.infrastructure.db_orm.tables.tbl_users import TblUsers
from src.application.crypt.crypt_service import CryptService


def populate_db():
    obj_user = TblUsers()
    obj_user.username = 'john.doe'
    obj_user.name = "john doe"
    obj_user.password = CryptService.encrypt('123')

    insert_obj(obj=obj_user)
