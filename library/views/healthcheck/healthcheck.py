from fastapi import APIRouter, HTTPException

from library.views.book.shemas import BookGetOutput, Message

health_check = APIRouter()


@health_check.get(
    path='/health_check',
    status_code=200,
    tags=["health_check"],
    description='Health-check Endpoint')
def health_check():
    return True
