from fastapi import status
from fastapi.testclient import TestClient

from src.domain.user import User


def test_post_route_token_with_valid_user_return_token(test_client: TestClient, created_user: User):
    url = f'/token'
    data = {'username': created_user.username, 'password': created_user.password}
    response = test_client.post(url=url, data=data)

    assert response.status_code == status.HTTP_201_CREATED
