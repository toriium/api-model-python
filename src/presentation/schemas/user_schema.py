from pydantic import BaseModel
from datetime import date


class FindUserInput(BaseModel):
    username: str
    password: str


class CreateUserInput(BaseModel):
    username: str
    name: str
    password: str


class CreateUserOutput(BaseModel):
    username: str
    name: str
    password: str
