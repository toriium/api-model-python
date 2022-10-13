import pytest
import httpx

from src.presentation.schemas.user_schema import CreateUserInput


def test_post_route_user_with_valid_data_return_200(host: str):
    user_data = {"username": 'platos', "name": 'platao', "password": '123'}
    response = httpx.post(url=f'{host}/user', json=user_data)
    print(response.json())
    assert response.status_code == 200
