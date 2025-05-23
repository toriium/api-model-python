
from src.application.book.book_error import BookError
from src.data.errors.repository_error import RepositoryError
from src.data.repository.books_repository import BooksRepository
from src.domain.book import BookDomain
from src.presentation.schemas.book_schema import CreateBookInput, UpdateBookInput


class BookService:
    @staticmethod
    def find_book_by_id(book_id: int) -> tuple[BookDomain | None, BookError | None]:
        found_book, error = BooksRepository.find_book_by_id(book_id=book_id)

        if not found_book:
            return None, None

        return BookDomain(**found_book.model_dump()), None

    @staticmethod
    def insert_book(data: CreateBookInput) -> tuple[BookDomain | None, BookError | None]:
        new_book = BookDomain(**data.model_dump())

        new_book, error = BooksRepository.insert_book(book=new_book)
        if error:
            if error == RepositoryError.duplicate_entry:
                return None, BookError.duplicate_entry

        return BookDomain(**new_book.model_dump()), None

    @staticmethod
    def update_book(data: UpdateBookInput) -> tuple[BookDomain | None, BookError | None]:
        target_book = BookDomain(**data.model_dump())

        updated_book, error = BooksRepository.update_book(book=target_book)
        if error:
            return None, BookError.not_found

        return BookDomain(**updated_book.model_dump()), None

    @staticmethod
    def delete_book(book_id) -> BookError | None:
        error = BooksRepository.delete_book(book_id=book_id)
        if error == RepositoryError.not_found:
            return BookError.not_found
        return None
