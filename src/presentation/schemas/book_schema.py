from pydantic import BaseModel
from datetime import date


class GETBookOutput(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str


class POSTBookInput(BaseModel):
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str


class POSTBookOutput(BaseModel):
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str
