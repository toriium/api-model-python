import httpx
from fastapi import status


def test_get_route_health_check_with_must_return_200_status_code(host):
    response = httpx.get(url=f'{host}/health_check')
    assert response.status_code == status.HTTP_200_OK
