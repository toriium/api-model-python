from src.domain.book import Book
from src.infrastructure.repository.books_repository import BooksRepository


class BookService:
    @staticmethod
    def find_book_by_id(book_id: int) -> Book:
        return BooksRepository.find_book_by_id(book_id=book_id)
