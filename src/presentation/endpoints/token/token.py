from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.application.token.token_service import create_access_token, get_current_user
from src.application.user.user_error import UserError
from src.application.user.user_service import UserService
from src.domain.user import UserDomain
from src.presentation.schemas.token import Token

token_router = APIRouter(prefix='/auth', tags=['auth'])


@token_router.post("/token", response_model=Token)
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

    access_token = create_access_token(data={'sub': user.username})

    return JSONResponse(content={"access_token": access_token, "token_type": "bearer"},
                        status_code=status.HTTP_201_CREATED)


@token_router.post('/refresh_token', response_model=Token)
async def refresh_access_token(user: UserDomain = Depends(get_current_user)):
    new_access_token = create_access_token(data={'sub': user.username})

    return JSONResponse(content={"access_token": new_access_token, "token_type": "bearer"},
                        status_code=status.HTTP_201_CREATED)

