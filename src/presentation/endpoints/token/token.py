from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.application.token.token_service import TokenService
from src.application.user.user_error import UserError
from src.application.user.user_service import UserService
from src.tracing import tracer_endpoint

token_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def token_validation(token: str = Depends(oauth2_scheme)):
    valid = TokenService.token_is_valid(token=token)
    if valid:
        return True
    else:
        raise HTTPException(detail="Invalid Token",status_code=status.HTTP_401_UNAUTHORIZED)


@token_router.post("/token")
@tracer_endpoint()
async def create_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user, error = UserService.user_is_valid(username=form_data.username, password=form_data.password)
    if error:
        if error == UserError.user_not_found:
            return HTTPException(detail={"message": "This user does't exist in our base"},
                                 status_code=status.HTTP_404_NOT_FOUND)
        if error == UserError.incorrect_password:
            return HTTPException(detail={"message": "Incorrect password"}, status_code=status.HTTP_400_BAD_REQUEST)

    token = TokenService.create_token()

    return JSONResponse(content={"access_token": token, "token_type": "bearer"}, status_code=status.HTTP_201_CREATED)
