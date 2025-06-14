from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from src.application.book.book_error import BookError
from src.application.book.book_service import BookService
from src.application.token.token_service import bearer_token_validation
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
    path="/book",
    response_model=FindBookOutput,
    status_code=200,
    dependencies=[Depends(bearer_token_validation)],
    responses={404: {"model": Message}, 500: {"model": Message}},
    tags=["book"],
    description="Get one Book",
)
async def get_book(book_id: int):
    result, error = BookService.find_book_by_id(book_id=book_id)
    if result:
        return JSONResponse(content=FindBookOutput(**result.model_dump()).model_dump(), status_code=status.HTTP_200_OK)

    return JSONResponse(content={"message": "Not found book with this id"}, status_code=status.HTTP_404_NOT_FOUND)


@book_router.post(
    path="/book",
    response_model=CreateBookOutput,
    status_code=201,
    dependencies=[Depends(bearer_token_validation)],
    responses={404: {"model": Message}, 500: {"model": Message}},
    tags=["book"],
    description="Create a Book",
)
async def create_book(payload: CreateBookInput):
    book, error = BookService.insert_book(data=payload)
    if error:
        if error == BookError.duplicate_entry:
            return JSONResponse(
                content={"message": "This book alredy exists in our base"}, status_code=status.HTTP_400_BAD_REQUEST
            )

    return JSONResponse(content=CreateBookOutput(**book.model_dump()).model_dump(), status_code=status.HTTP_201_CREATED)


@book_router.put(
    path="/book",
    response_model=UpdateBookOutput,
    status_code=200,
    dependencies=[Depends(bearer_token_validation)],
    responses={404: {"model": Message}, 500: {"model": Message}},
    tags=["book"],
    description="Update a Book",
)
async def update_book(payload: UpdateBookInput):
    book, error = BookService.update_book(data=payload)
    if error:
        if error == BookError.not_found:
            return JSONResponse(content={"message": "Book not found"}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(UpdateBookOutput(**book.model_dump()).model_dump(), status_code=status.HTTP_200_OK)


@book_router.delete(
    path="/book",
    response_model=Message,
    status_code=200,
    dependencies=[Depends(bearer_token_validation)],
    responses={404: {"model": Message}, 500: {"model": Message}},
    tags=["book"],
    description="Delete a Book",
)
async def delete_book(book_id: int):
    error = BookService.delete_book(book_id=book_id)
    if error:
        if error == BookError.not_found:
            return JSONResponse(content={"message": "Book not found"}, status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content={"message": "Book deleted"}, status_code=status.HTTP_200_OK)
