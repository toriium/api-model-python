from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from src.application.user.user_error import UserError
from src.application.user.user_service import UserService
from src.presentation.schemas.user_schema import POSTUserInput, POSTUserOutput
from src.presentation.schemas.message_schema import Message

user_router = APIRouter()


@user_router.post(
    path='/user',
    response_model=POSTUserInput,
    status_code=200,
    # dependencies=[Depends(validate_authorization)],
    responses={404: {"model": Message},
               500: {"model": Message}},
    tags=["user"],
    description='Endpoint to create a User'
)
def create_user(payload: POSTUserInput):
    try:
        user, error = UserService.create_user(payload)
        if error:
            if error == UserError.duplicate_entry:
                return JSONResponse(status_code=400, content={"message": "This user alredy exist in our base"})

        return POSTUserOutput(**user.dict())

    except Exception as error:
        print(error)
        raise HTTPException(500, detail={"message": "Error ocured in the middle of process"})
