from fastapi import APIRouter, status
from starlette.responses import HTMLResponse

home_router = APIRouter()


@home_router.get(
    path="/",
    status_code=200,
    tags=["home"],
    description="/",
)
async def home():
    return HTMLResponse(
        content="<h1>Welcome to the Book API</h1><p>Use the /book endpoint to manage books.</p>",
        status_code=status.HTTP_200_OK,
    )
