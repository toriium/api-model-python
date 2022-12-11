import pytest
import httpx

from src.domain.user import User


def test_post_route_token_with_valid_user_return_token(host: str, created_user: User):
    data = {'username': created_user.username, 'password': created_user.password}
    response = httpx.post(url=f'{host}/token', data=data)
    assert response.status_code == 200
