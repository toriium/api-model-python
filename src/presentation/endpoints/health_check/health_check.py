from fastapi import APIRouter

from src.tracing import tracer_endpoint

health_check_router = APIRouter()


@health_check_router.get(
    path='/health_check',
    status_code=200,
    tags=["health_check"],
    description='Health-check Endpoint')
@tracer_endpoint()
async def health_check():
    return True
