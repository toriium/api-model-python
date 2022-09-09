from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from src.schemas.book_schema import GetBookOutput
from src.schemas.message_schema import Message

from src.application.book.book_service import BookService

book_router = APIRouter()


@book_router.get(
    path='/book',
    response_model=GetBookOutput,
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
            return GetBookOutput(**result.dict())
        else:
            return JSONResponse(status_code=404, content={"message": "Not found book with this id"})
    except Exception as error:
        # add_log(traceback.format_exc())
        raise HTTPException(500, detail={"message": "Error ocured in the middle of process"})
