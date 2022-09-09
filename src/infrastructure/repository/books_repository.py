from src.infrastructure.database.tables.books import Books
from src.infrastructure.database.query_obj import select_first_obj, select_all_obj

from src.domain.book import Book


class BooksRepository:
    @staticmethod
    def find_book_by_id(book_id: int) -> Book:
        query_result = select_first_obj(obj=Books, kw_filters={"id": book_id})
        return Book(**query_result.to_dict())

    @staticmethod
    def find_book_by_isnp(isnp: str) -> Book:
        query_result = select_first_obj(obj=Books, kw_filters={"isnp": isnp})
        return Book(**query_result.to_dict())

    @staticmethod
    def find_book_by_name(name: str) -> Book:
        query_result = select_first_obj(obj=Books, kw_filters={"name": name})
        return Book(**query_result.to_dict())

    @staticmethod
    def find_books_by_author(author: str) -> list[Book]:
        books = []
        query_result = select_all_obj(obj=Books, kw_filters={"author": author})
        for value in query_result:
            books.append(Book(**value.to_dict()))
        return books

    @staticmethod
    def find_books_by_publisher(publisher: str) -> list[Book]:
        books = []
        query_result = select_all_obj(obj=Books, kw_filters={"publisher": publisher})
        for value in query_result:
            books.append(Book(**value.to_dict()))
        return books
