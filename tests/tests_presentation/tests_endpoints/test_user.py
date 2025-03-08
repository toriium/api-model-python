from fastapi import status
from starlette.testclient import TestClient

from src.application.user.user_service import UserService
from src.domain.user import UserDomain


def test_post_route_user_with_valid_data_return_200(test_client: TestClient, fake):
    url = '/user'
    json_data = {"username": fake.name(), "name": fake.name(), "password": fake.text()}

    response = test_client.post(url=url, json=json_data)

    UserService.delete_user_by_username(username=json_data['username'])

    assert response.status_code == status.HTTP_201_CREATED


def test_delete_route_user_with_valid_username_return_200(test_client: TestClient, fake, created_user: UserDomain):
    url = '/user'
    params = {"username": created_user.username}

    response = test_client.delete(url=url, params=params)

    expected_response = {"message": "User deleted"}

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_response
