from faker import Faker
from pytest import fixture
from fastapi.testclient import TestClient

from src.main import app
from src.application.book.book_service import BookService
from src.application.token.token_service import TokenService
from src.application.user.user_service import UserService
from src.domain.book import BookDomain
from src.domain.user import UserDomain
from src.presentation.schemas.book_schema import CreateBookInput
from src.presentation.schemas.user_schema import CreateUserInput


@fixture(scope="session")
def test_client() -> TestClient:
    return TestClient(app=app)


@fixture(scope="session")
def fake() -> Faker:
    return Faker()


@fixture(scope="session")
def valid_headers() -> dict[str]:
    token = TokenService.create_token()
    return {"Authorization": f'Bearer {token}'}


@fixture(scope="function")
def created_user(fake) -> UserDomain:
    user_input = CreateUserInput(username=fake.name(), name=fake.name(), password=fake.random_int())
    new_user, error = UserService.create_user(received_user=user_input)
    yield new_user
    UserService.delete_user_by_username(username=user_input.username)


@fixture(scope="function")
def created_book(fake) -> BookDomain:
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
