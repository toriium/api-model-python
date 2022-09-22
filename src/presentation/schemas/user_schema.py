from pydantic import BaseModel
from datetime import date


class GETUserInput(BaseModel):
    username: str
    password: str


class POSTUserInput(BaseModel):
    username: str
    name: str
    password: str


class POSTUserOutput(BaseModel):
    username: str
    name: str
    password: str
