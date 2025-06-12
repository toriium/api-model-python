from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt import DecodeError, ExpiredSignatureError, decode, encode
from pwdlib import PasswordHash

from src.application.user.user_service import UserService
from src.domain.user import UserDomain
from src.settings import TokenEnv

pwd_context = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(minutes=TokenEnv.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, TokenEnv.SECRET_KEY, algorithm=TokenEnv.ALGORITHM)
    return encoded_jwt


async def token_is_valid(token: str) -> str:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode(jwt=token, key=TokenEnv.SECRET_KEY, algorithms=[TokenEnv.ALGORITHM])
        subject = payload.get("sub")

        if not subject:
            raise credentials_exception

    except DecodeError:
        raise credentials_exception

    except ExpiredSignatureError:
        raise credentials_exception

    return subject


async def token_validation(token: str = Depends(oauth2_scheme)):
    await token_is_valid(token)


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserDomain:
    subject = await token_is_valid(token)

    user, err = UserService.get_user_by_username(username=subject)

    if not user:
        raise err

    return user
