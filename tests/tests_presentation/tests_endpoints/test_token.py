import pytest
import httpx

from src.domain.user import User


def test_post_route_token_with_valid_user_return_token(host: str, valid_user: User):
    data = {'username': valid_user.username, 'password': valid_user.password}
    response = httpx.post(url=f'{host}/token', data=data)
    assert response.status_code == 200
