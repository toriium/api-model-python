import traceback

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from library.views.books.shemas import BookGetOutput, Message

book_router = APIRouter()


@book_router.get(
    path='/book',
    response_model=BookGetOutput,
    status_code=200,
    # dependencies=[Depends(validate_authorization)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["books"],
    description='Endpoint to get customer with bad credit, searching by customer_document')
def consult_by_customer_document():
    try:
        return 'this is a response'
        # return JSONResponse(status_code=404, content={"message": "Customer does't have bad credit"})
    except Exception as error:
        # add_log(traceback.format_exc())
        raise HTTPException(500, detail={"message": "Error ocured in the middle of process"})
