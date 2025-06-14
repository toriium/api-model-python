from pydantic import BaseModel


class TokenOutput(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
