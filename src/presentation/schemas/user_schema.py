from pydantic import BaseModel
from datetime import date


class POSTUserInput(BaseModel):
    username: str
    name: str
    password: str


class POSTUserOutput(BaseModel):
    username: str
    name: str
    password: str
