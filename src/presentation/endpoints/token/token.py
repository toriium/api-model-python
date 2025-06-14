from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordRequestFormStrict
from pydantic import BaseModel

from src.application.token.token_service import create_access_token, create_refresh_token, get_current_user, token_is_valid
from src.application.user.user_error import UserError
from src.application.user.user_service import UserService
from src.domain.user import UserDomain
from src.presentation.schemas.token import TokenOutput

token_router = APIRouter(prefix='/auth', tags=['auth'])


@token_router.post("/token", response_model=TokenOutput)
async def create_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user, error = UserService.get_user_by_username(username=form_data.username)
    if error:
        if error == UserError.user_not_found:
            return HTTPException(
                detail={"message": "This user does't exist in our base"},
                status_code=status.HTTP_404_NOT_FOUND
            )
        if error == UserError.incorrect_password:
            return HTTPException(detail={"message": "Incorrect password"},
                                 status_code=status.HTTP_400_BAD_REQUEST)

    access_token, jwt_data = create_access_token(username=user.username)
    refresh_token = create_refresh_token(username=user.username)


    response_data = TokenOutput(
        access_token=access_token,
        token_type="bearer",
        expires_in=jwt_data.exp,
        refresh_token=refresh_token
    )

    return JSONResponse(content=response_data.model_dump(), status_code=status.HTTP_201_CREATED)


class RefreshTokenForm(BaseModel):
    refresh_token: str

@token_router.post('/refresh_token', response_model=TokenOutput)
async def refresh_access_token(form_data: RefreshTokenForm):

    username = await token_is_valid(token=form_data.refresh_token)

    new_access_token, jwt_data = create_access_token(username=username)
    refresh_token = create_refresh_token(username=username)


    response_data = TokenOutput(
        access_token=new_access_token,
        token_type="bearer",
        expires_in=jwt_data.exp,
        refresh_token=refresh_token
    )

    return JSONResponse(content=response_data.model_dump(), status_code=status.HTTP_201_CREATED)

