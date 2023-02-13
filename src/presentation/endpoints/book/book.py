from fastapi import APIRouter, Depends
from starlette.responses import JSONResponse

from src.application.book.book_error import BookError
from src.application.book.book_service import BookService
from src.presentation.endpoints.token.token import token_validation
from src.presentation.schemas.book_schema import (
    CreateBookInput,
    CreateBookOutput,
    FindBookOutput,
    UpdateBookInput,
    UpdateBookOutput,
)
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
    description='Get one Book'
)
async def get_book(book_id: int):
    result, error = BookService.find_book_by_id(book_id=book_id)
    if result:
        return FindBookOutput(**result.dict())
    else:
        return JSONResponse(status_code=404, content={"message": "Not found book with this id"})


@book_router.post(
    path='/book',
    response_model=CreateBookOutput,
    status_code=201,
    dependencies=[Depends(token_validation)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["book"],
    description='Create a Book'
)
async def create_book(payload: CreateBookInput):
    book, error = BookService.insert_book(data=payload)
    if error:
        if error == BookError.duplicate_entry:
            return JSONResponse(status_code=400, content={"message": "This book alredy exists in our base"})

    return CreateBookOutput(**book.dict())


@book_router.put(
    path='/book',
    response_model=UpdateBookOutput,
    status_code=200,
    dependencies=[Depends(token_validation)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["book"],
    description='Update a Book'
)
async def update_book(payload: UpdateBookInput):
    book, error = BookService.update_book(data=payload)
    if error:
        if error == BookError.not_found:
            return JSONResponse(status_code=404, content={"message": "Book not found"})

    return UpdateBookOutput(**book.dict())


@book_router.delete(
    path='/book',
    response_model=Message,
    status_code=200,
    dependencies=[Depends(token_validation)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["book"],
    description='Delete a Book'
)
async def delete_book(book_id: int):
    error = BookService.delete_book(book_id=book_id)
    if error:
        if error == BookError.not_found:
            return JSONResponse(status_code=404, content={"message": "Book not found"})

    return JSONResponse(status_code=200, content={"message": "Book deleted"})
