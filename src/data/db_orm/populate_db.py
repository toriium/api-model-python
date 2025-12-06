from src.application.crypt.crypt_service import CryptService
from src.data.db_orm.query_obj import insert_obj
from src.data.db_orm.tables.tbl_books import TblBooks
from src.data.db_orm.tables.tbl_users import TblUsers
from src.data.errors.sql_error import SQLError


def add_tbl_users() -> list:
    user1 = TblUsers(username='john.doe',
                     name='john doe',
                     password=CryptService.encrypt('123'),
                     )
    book1 = TblBooks(
        isbn='978-3328109211',
        name='Also sprach Zarathustra',
        author='Friedrich Nietzsche ',
        publisher='Penguin TB Verlag',
        release_date='13 octubre 2022',
        pages=432,
        description='This guy is crazy.'
    )

    commands = [
        user1,
        book1
    ]
    return commands


def populate_db():
    objs = []

    objs.extend(add_tbl_users())

    for obj in objs:
        updated, err = insert_obj(obj)
        if err:
            if err == SQLError.duplicate_entry:
                continue
            else:
                raise err
