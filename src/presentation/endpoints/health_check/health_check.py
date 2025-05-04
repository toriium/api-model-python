from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

health_check_router = APIRouter()


@health_check_router.get(
    path='/health_check',
    status_code=200,
    tags=["health_check"],
    description='Health-check Endpoint')
async def health_check():
    return JSONResponse(content={'message': 'I am still working'},status_code=status.HTTP_200_OK)
