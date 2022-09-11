from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from src.application.errors.application_error import ApplicationError
from src.presentation.schemas.book_schema import GETBookOutput, POSTBookInput, POSTBookOutput
from src.presentation.schemas.message_schema import Message

from src.application.book.book_service import BookService

book_router = APIRouter()


@book_router.get(
    path='/book/{book_id}',
    response_model=GETBookOutput,
    status_code=200,
    # dependencies=[Depends(validate_authorization)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["books"],
    description='Endpoint to get Book'
)
def get_book(book_id: int):
    try:
        result = BookService.find_book_by_id(book_id=book_id)
        if result:
            return GETBookOutput(**result.dict())
        else:
            return JSONResponse(status_code=404, content={"message": "Not found book with this id"})
    except Exception as error:
        raise HTTPException(500, detail={"message": "Error ocured in the middle of process"})


@book_router.post(
    path='/book',
    response_model=POSTBookOutput,
    status_code=200,
    # dependencies=[Depends(validate_authorization)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["book"],
    description='Endpoint to create a Book'
)
def create_book(payload: POSTBookInput):
    try:
        result, error = BookService.insert_book(data=payload)
        if error:
            if error == ApplicationError.duplicate_entry:
                return JSONResponse(status_code=400, content={"message": "This book alredy exist in our base"})

        return POSTBookOutput(**result.dict())

    except Exception as error:
        raise HTTPException(500, detail={"message": "Error ocured in the middle of process"})
