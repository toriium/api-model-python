from typing import Union

from src.infrastructure.dtos.tbl_books_dto import TblBooksDTO
from src.infrastructure.errors.sql_error import SQLError
from src.infrastructure.db_orm.tables.tbl_books import TblBooks
from src.infrastructure.db_orm.query_obj import select_first_obj, select_all_obj, insert_obj

from src.domain.book import Book


class BooksRepository:
    @staticmethod
    def find_book_by_id(book_id: int) -> tuple[Union[TblBooksDTO, None], Union[SQLError, None]]:
        query_result = select_first_obj(obj_table=TblBooks, filter_by={"id": book_id})
        if query_result:
            return TblBooksDTO.from_orm(query_result), None
        else:
            return None, None

    @staticmethod
    def find_book_by_name(name: int) -> tuple[Union[TblBooksDTO, None], Union[SQLError, None]]:
        query_result = select_first_obj(obj_table=TblBooks, filter_by={"name": name})
        if query_result:
            return TblBooksDTO.from_orm(query_result), None
        else:
            return None, None

    @staticmethod
    def insert_book(book: Book) -> tuple[Union[TblBooksDTO, None], Union[SQLError, None]]:
        new_book = TblBooks()
        new_book.isbn = book.isbn
        new_book.name = book.name
        new_book.author = book.author
        new_book.publisher = book.publisher
        new_book.release_date = book.release_date
        new_book.pages = book.pages
        new_book.description = book.description

        query_result, error = insert_obj(obj=new_book)
        if error:
            if error == SQLError.duplicate_entry:
                return None, SQLError.duplicate_entry

        if query_result:
            return TblBooksDTO.from_orm(query_result), None
        else:
            return None, None
