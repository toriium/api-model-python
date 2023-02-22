from fastapi import APIRouter

from src.presentation.schemas.book_schema import FindBookOutput
from src.presentation.schemas.message_schema import Message
from src.tracing import tracer_endpoint

books_router = APIRouter()


@books_router.get(
    path='/books',
    response_model=FindBookOutput,
    status_code=200,
    # dependencies=[Depends(validate_authorization)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["books"],
    description='Endpoint to get customer with bad credit, searching by customer_document')
@tracer_endpoint()
async def consult_by_customer_document():
    return 'this is a response'

