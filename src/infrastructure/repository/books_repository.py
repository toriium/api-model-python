from typing import Union

from src.infrastructure.database.tables.books import Books
from src.infrastructure.database.query_obj import select_first_obj, select_all_obj

from src.domain.book import Book


class BooksRepository:
    @staticmethod
    def find_book_by_id(book_id: int) -> Union[Book, None]:
        query_result = select_first_obj(obj=Books, kw_filters={"id": book_id})
        if query_result:
            return Book(**query_result.to_dict())
        else:
            return None

    @staticmethod
    def find_book_by_isnp(isnp: str) -> Union[Book, None]:
        query_result = select_first_obj(obj=Books, kw_filters={"isnp": isnp})
        if query_result:
            return Book(**query_result.to_dict())
        else:
            return None

    @staticmethod
    def find_book_by_name(name: str) -> Union[Book, None]:
        query_result = select_first_obj(obj=Books, kw_filters={"name": name})
        if query_result:
            return Book(**query_result.to_dict())
        else:
            return None

    @staticmethod
    def find_books_by_author(author: str) -> Union[list[Book], None]:
        books = []
        query_result = select_all_obj(obj=Books, kw_filters={"author": author})
        if query_result:
            for value in query_result:
                books.append(Book(**value.to_dict()))
            return books
        else:
            return None

    @staticmethod
    def find_books_by_publisher(publisher: str) -> Union[list[Book], None]:
        books = []
        query_result = select_all_obj(obj=Books, kw_filters={"publisher": publisher})
        if query_result:
            for value in query_result:
                books.append(Book(**value.to_dict()))
            return books
        else:
            return None

