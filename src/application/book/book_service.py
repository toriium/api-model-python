from src.domain.book import Book
from src.infrastructure.repository.books_repository import BooksRepository
from src.presentation.schemas.book_schema import POSTBookInput


class BookService:
    @staticmethod
    def find_book_by_id(book_id: int) -> Book:
        return BooksRepository.find_book_by_id(book_id=book_id)

    @staticmethod
    def insert_book(data: POSTBookInput) -> Book:
        new_book = Book(**data.dict())
        return BooksRepository.insert_book(book=new_book)
