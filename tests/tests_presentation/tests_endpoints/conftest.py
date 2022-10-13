from pytest import fixture

from src.application.token.token_service import TokenService
from src.application.user.user_service import UserService
from src.application.product.product_service import ProductService
from src.domain.user import User
from src.domain.product import Product
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
    return TokenService.create_token()


@fixture(scope="session")
def valid_product() -> Product:
    produc_id = 1
    product, error = ProductService.find_product_by_id(product_id=produc_id)
    return product


@fixture(scope="session")
def unexistent_product_id():
    produc_id = 5481285
    return produc_id
