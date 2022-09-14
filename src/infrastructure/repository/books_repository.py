from typing import Union

from src.infrastructure.errors.sql_error import SQLError
from src.infrastructure.db_orm.tables.tbl_books import TblBooks
from src.infrastructure.db_orm.query_obj import select_first_obj, select_all_obj, insert_obj

from src.domain.book import Book


class BooksRepository:
    @staticmethod
    def find_book_by_id(book_id: int) -> Union[Book, None]:
        query_result = select_first_obj(obj_table=TblBooks, kw_filters={"id": book_id})
        if query_result:
            return Book(**query_result.to_dict())
        else:
            return None

    @staticmethod
    def find_book_by_isnp(isnp: str) -> Union[Book, None]:
        query_result = select_first_obj(obj_table=TblBooks, kw_filters={"isnp": isnp})
        if query_result:
            return Book(**query_result.to_dict())
        else:
            return None

    @staticmethod
    def find_book_by_name(name: str) -> Union[Book, None]:
        query_result = select_first_obj(obj_table=TblBooks, kw_filters={"name": name})
        if query_result:
            return Book(**query_result.to_dict())
        else:
            return None

    @staticmethod
    def find_books_by_author(author: str) -> Union[list[Book], None]:
        books = []
        query_result = select_all_obj(obj_table=TblBooks, kw_filters={"author": author})
        if query_result:
            for value in query_result:
                books.append(Book(**value.to_dict()))
            return books
        else:
            return None

    @staticmethod
    def find_books_by_publisher(publisher: str) -> Union[list[Book], None]:
        books = []
        query_result = select_all_obj(obj_table=TblBooks, kw_filters={"publisher": publisher})
        if query_result:
            for value in query_result:
                books.append(Book(**value.to_dict()))
            return books
        else:
            return None

    @staticmethod
    def insert_book(book: Book) -> tuple[Union[dict, None], Union[SQLError, None]]:
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
            return query_result.to_dict(), None
        else:
            return None, None
