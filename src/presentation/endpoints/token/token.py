
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.application.token.token_service import TokenService
from src.application.user.user_error import UserError
from src.application.user.user_service import UserService

token_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def token_validation(token: str = Depends(oauth2_scheme)):
    valid = TokenService.token_is_valid(token=token)
    if valid:
        return True
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")


@token_router.post("/token")
async def create_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user, error = UserService.user_is_valid(username=form_data.username, password=form_data.password)
    if error:
        if error == UserError.user_not_found:
            return HTTPException(status_code=404, detail={"message": "This user does't exist in our base"})
        if error == UserError.incorrect_password:
            return HTTPException(status_code=400, detail={"message": "Incorrect password"})

    token = TokenService.create_token()

    return {"access_token": token, "token_type": "bearer"}
