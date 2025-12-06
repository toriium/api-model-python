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
        isbn='978-3-16-148410-0',
        name='Example Book',
        author='Author Name',
        publisher='Publisher Name',
        release_date='2023-01-01',
        pages=350,
        description='This is an example book description.'
    )

    commands = [
        user1,
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
