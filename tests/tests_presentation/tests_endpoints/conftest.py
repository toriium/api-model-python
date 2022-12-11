from datetime import date

from pytest import fixture
from faker import Faker

from src.application.token.token_service import TokenService
from src.application.user.user_service import UserService
from src.application.book.book_service import BookService
from src.domain.user import User
from src.domain.book import Book
from src.presentation.schemas.book_schema import CreateBookInput
from src.presentation.schemas.user_schema import CreateUserInput


@fixture
def host() -> str:
    return f"http://localhost:8080"


@fixture(scope="session")
def valid_user() -> User:
    user_input = CreateUserInput(username='geraldo01', name='geraldo', password='123')
    new_user, error = UserService.create_user(received_user=user_input)
    return new_user


@fixture(scope="session")
def valid_token() -> str:
    token = TokenService.create_token()
    return f'Bearer {token}'


@fixture(scope="session")
def valid_headers() -> dict[str]:
    token = TokenService.create_token()
    return {"Authorization": f'Bearer {token}'}


@fixture(scope="function")
def created_book() -> Book:
    fake = Faker()

    book = CreateBookInput(
        isbn=fake.isbn13(),
        name=fake.name(),
        author=fake.name(),
        publisher=fake.company(),
        release_date=fake.date_object(),
        pages=fake.random_int(),
        description=fake.text()
    )
    book, _ = BookService.insert_book(data=book)
    yield book
    BookService.delete_book(book_id=book.id)


@fixture(scope="session")
def unexistent_book_id():
    book_id = 5481285
    return book_id
