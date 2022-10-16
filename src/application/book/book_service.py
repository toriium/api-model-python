from typing import Optional

from src.application.book.book_error import BookError
from src.domain.book import Book
from src.infrastructure.repository.books_repository import BooksRepository
from src.infrastructure.errors.sql_error import SQLError
from src.presentation.schemas.book_schema import CreateBookInput


class BookService:
    @staticmethod
    def find_book_by_id(book_id: int) -> Optional[Book]:
        found_book, error = BooksRepository.find_book_by_id(book_id=book_id)

        if not found_book:
            return None

        return Book(**found_book.dict())

    @staticmethod
    def insert_book(data: CreateBookInput) -> tuple[Optional[Book], Optional[BookError]]:
        new_book = Book(**data.dict())

        new_book, error = BooksRepository.insert_book(book=new_book)
        if error:
            if error == SQLError.duplicate_entry:
                return None, BookError.duplicate_entry

        return Book(**new_book.dict()), None
