from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import JSONResponse

from src.application.book.book_error import BookError
from src.application.book.book_service import BookService
from src.presentation.endpoints.token.token import token_validation
from src.presentation.schemas.book_schema import FindBookOutput, CreateBookInput, CreateBookOutput
from src.presentation.schemas.message_schema import Message

book_router = APIRouter()


@book_router.get(
    path='/book/{book_id}',
    response_model=FindBookOutput,
    status_code=200,
    dependencies=[Depends(token_validation)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["book"],
    description='Endpoint to get Book'
)
async def get_book(book_id: int):
    result = BookService.find_book_by_id(book_id=book_id)
    if result:
        return FindBookOutput(**result.dict())
    else:
        return JSONResponse(status_code=404, content={"message": "Not found book with this id"})


@book_router.post(
    path='/book',
    response_model=CreateBookOutput,
    status_code=200,
    dependencies=[Depends(token_validation)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["book"],
    description='Endpoint to create a Book'
)
def create_book(payload: CreateBookInput):
    book, error = BookService.insert_book(data=payload)
    if error:
        if error == BookError.duplicate_entry:
            return JSONResponse(status_code=400, content={"message": "This book alredy exist in our base"})

    return CreateBookOutput(**book.dict())
