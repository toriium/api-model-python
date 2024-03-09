from fastapi import status
from fastapi.testclient import TestClient


def test_get_route_health_check_with_must_return_200_status_code(test_client: TestClient):
    url = '/health_check'
    response = test_client.get(url=url)

    assert response.status_code == status.HTTP_200_OK
