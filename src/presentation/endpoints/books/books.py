from fastapi import APIRouter, Depends

from src.application.token.token_service import bearer_token_validation
from src.presentation.schemas.book_schema import FindBookOutput
from src.presentation.schemas.message_schema import Message

books_router = APIRouter()


@books_router.get(
    path="/books",
    response_model=FindBookOutput,
    status_code=200,
    dependencies=[Depends(bearer_token_validation)],
    responses={404: {"model": Message}, 500: {"model": Message}},
    tags=["books"],
    description="Endpoint to get customer with bad credit, searching by customer_document",
)
async def consult_by_customer_document():
    return "this is a response"
