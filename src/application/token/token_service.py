from typing import Union

from src.application.token.token_error import TokenError
from src.infrastructure.repository.books_repository import BooksRepository
from src.infrastructure.errors.sql_error import SQLError


class TokenService:
    ...
    # @staticmethod
    # def valid_credentials(username: str, password: str) -> ...:
    #     return BooksRepository.find_book_by_id(book_id=book_id)
    #
    # @staticmethod
    # def create_new_valid_token(username: str, password: str) -> ...:
    #     return BooksRepository.find_book_by_id(book_id=book_id)


