from datetime import date

from pydantic import BaseModel, validator


class FindBookOutput(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str

    @validator('release_date')
    def username_alphanumeric(cls, v:date):
        return v.isoformat()


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

    @validator('release_date')
    def username_alphanumeric(cls, v:date):
        return v.isoformat()


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

    @validator('release_date')
    def username_alphanumeric(cls, v:date):
        return v.isoformat()
