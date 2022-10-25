from pydantic import BaseModel
from datetime import date


class FindBookOutput(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str


class CreateBookInput(BaseModel):
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str


class CreateBookOutput(BaseModel):
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str


class UpdateBookInput(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str


class UpdateBookOutput(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str
