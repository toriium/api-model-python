from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from src.application.user.user_error import UserError
from src.application.user.user_service import UserService
from src.presentation.schemas.message_schema import Message
from src.presentation.schemas.user_schema import CreateUserInput, CreateUserOutput, FindUserInput
from src.tracing import tracer_endpoint

user_router = APIRouter()


@user_router.get(
    path='/user',
    response_model=Message,
    status_code=200,
    dependencies=[],
    responses={404: {"model": Message},
               400: {"model": Message},
               500: {"model": Message}},
    tags=["user"],
    description='Validate your User'
)
@tracer_endpoint()
async def validate_user(payload: FindUserInput):
    user, error = UserService.user_is_valid(username=payload.username, password=payload.password)
    if error:
        if error == UserError.user_not_found:
            return JSONResponse(content={"message": "This user does't exist in our base"}, status_code=status.HTTP_404_NOT_FOUND)
        if error == UserError.incorrect_password:
            return JSONResponse(content={"message": "Incorrect password"}, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content={"message": "This user is valid"}, status_code=status.HTTP_200_OK)


@user_router.post(
    path='/user',
    response_model=CreateUserInput,
    status_code=200,
    dependencies=[],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["user"],
    description='Create an User'
)
@tracer_endpoint()
async def create_user(payload: CreateUserInput):
    user, error = UserService.create_user(payload)
    if error:
        if error == UserError.duplicate_entry:
            return JSONResponse(content={"message": "This user alredy exist in our base"},
                                status_code=status.HTTP_400_BAD_REQUEST)

    return CreateUserOutput(**user.dict())


@user_router.delete(
    path='/user',
    response_model=Message,
    status_code=200,
    dependencies=[],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["user"],
    description='Delete an User'
)
@tracer_endpoint()
async def delete_user(username: str):
    error = UserService.delete_user_by_username(username=username)
    if error:
        if error == UserError.not_found:
            return JSONResponse(content={"message": "User not found"}, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content={"message": "User deleted"}, status_code=status.HTTP_200_OK)
