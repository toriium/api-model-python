import traceback

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse

from library.views.books.shemas import BookGetOutput, Message

book_router = APIRouter()


# @consult_router.get(
#     '/book/{customer_document}',
#     response_model=BookGetOutput,
#     responses={404: {"model": Message},
#                500: {"model": Message}},
#     # dependencies=[Depends(validate_authorization)],
#     description='Endpoint to get customer with bad credit, searching by customer_document')
# def consult_by_customer_document(customer_document: str):
#     try:
#        return {'dddddd'}
#     except Exception as error:
#         # add_log(traceback.format_exc())
#         raise HTTPException(500, detail={"message": "Error ocured in the middle of process"})


@book_router.get(
    '/book/'
)
def consult_by_customer_document(customer_document: str):
    try:
        return {'dddddd'}
    except Exception as error:
        raise HTTPException(500, detail={"message": "Error ocured in the middle of process"})
