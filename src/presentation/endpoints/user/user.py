from fastapi import APIRouter, HTTPException, Depends
from starlette.responses import JSONResponse

from src.application.user.user_error import UserError
from src.application.user.user_service import UserService
from src.presentation.schemas.user_schema import CreateUserInput, CreateUserOutput, FindUserInput
from src.presentation.schemas.message_schema import Message

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
def validate_user(payload: FindUserInput):
    user, error = UserService.user_is_valid(username=payload.username, password=payload.password)
    if error:
        if error == UserError.user_not_found:
            return JSONResponse(status_code=404, content={"message": "This user does't exist in our base"})
        if error == UserError.incorrect_password:
            return JSONResponse(status_code=400, content={"message": "Incorrect password"})

    return JSONResponse(status_code=200, content={"message": "This user is valid"})


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
async def create_user(payload: CreateUserInput):
    user, error = UserService.create_user(payload)
    if error:
        if error == UserError.duplicate_entry:
            return JSONResponse(status_code=400, content={"message": "This user alredy exist in our base"})

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
async def create_user(username: str):
    error = UserService.delete_user_by_username(username=username)
    if error:
        if error == UserError.not_found:
            return JSONResponse(status_code=400, content={"message": "User not found"})

    return JSONResponse(status_code=200, content={"message": "User deleted"})
