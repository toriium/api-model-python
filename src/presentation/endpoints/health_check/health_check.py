from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.tracing import tracer_endpoint

health_check_router = APIRouter()


@health_check_router.get(
    path='/health_check',
    status_code=200,
    tags=["health_check"],
    description='Health-check Endpoint')
@tracer_endpoint()
async def health_check():
    return JSONResponse(content={'message': 'I still working'},status_code=status.HTTP_200_OK)
