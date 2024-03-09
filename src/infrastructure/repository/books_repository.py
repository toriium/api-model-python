
from src.domain.book import BookDomain
from src.infrastructure.db_orm.query_obj import delete_obj, insert_obj, select_first_obj, update_obj
from src.infrastructure.db_orm.tables.tbl_books import TblBooks
from src.infrastructure.dtos.books_dto import BookDTO
from src.infrastructure.errors.sql_error import SQLError
from src.infrastructure.redis.cache_expiration import CacheExpiration
from src.infrastructure.redis.decorators import delete_cached_value, get_cached_value_2_returns


class BooksRepository:
    @staticmethod
    @get_cached_value_2_returns(key="book-id-{book_id}", expiration=CacheExpiration.ONE_HOUR)
    def find_book_by_id(book_id: int) -> tuple[BookDTO | None, SQLError | None]:
        query_result = select_first_obj(obj_table=TblBooks, filter_by={"id": book_id})
        if query_result:
            return BookDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def find_book_by_name(name: int) -> tuple[BookDTO | None, SQLError | None]:
        query_result = select_first_obj(obj_table=TblBooks, filter_by={"name": name})
        if query_result:
            return BookDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def insert_book(book: BookDomain) -> tuple[BookDTO | None, SQLError | None]:
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
            return BookDTO.model_validate(query_result), None
        else:
            return None, None

    @staticmethod
    def update_book(book: BookDomain) -> tuple[BookDTO | None, SQLError | None]:
        obj_update = book.dict()
        query_result, error = update_obj(TblBooks, filter_by={"id": book.id}, obj_update=obj_update)
        if error:
            if error == SQLError.not_found:
                return None, SQLError.not_found

        if query_result:
            return BookDTO(**book.dict()), None
        else:
            return None, None

    @staticmethod
    @delete_cached_value(key="book-id-{book_id}")
    def delete_book(book_id: int) -> SQLError | None:
        error = delete_obj(obj_table=TblBooks, filter_by={"id": book_id})
        return error if error else None
