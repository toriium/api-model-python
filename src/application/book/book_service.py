from typing import Optional

from src.application.book.book_error import BookError
from src.domain.book import Book
from src.infrastructure.repository.books_repository import BooksRepository
from src.infrastructure.errors.sql_error import SQLError
from src.presentation.schemas.book_schema import CreateBookInput, UpdateBookInput


class BookService:
    @staticmethod
    def find_book_by_id(book_id: int) -> tuple[Optional[Book], Optional[BookError]]:
        found_book, error = BooksRepository.find_book_by_id(book_id=book_id)

        if not found_book:
            return None, None

        return Book(**found_book.dict()), None

    @staticmethod
    def insert_book(data: CreateBookInput) -> tuple[Optional[Book], Optional[BookError]]:
        new_book = Book(**data.dict())

        new_book, error = BooksRepository.insert_book(book=new_book)
        if error:
            if error == SQLError.duplicate_entry:
                return None, BookError.duplicate_entry

        return Book(**new_book.dict()), None

    @staticmethod
    def update_book(data: UpdateBookInput) -> tuple[Optional[Book], Optional[BookError]]:
        target_book = Book(**data.dict())

        updated_book, error = BooksRepository.update_book(book=target_book)
        if error:
            return None, BookError.not_found

        return Book(**updated_book.dict()), None

    @staticmethod
    def delete_book(book_id) -> Optional[BookError]:
        error = BooksRepository.delete_book(book_id=book_id)
        if error == SQLError.not_found:
            return BookError.not_found
