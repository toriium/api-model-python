from pydantic import BaseModel, validator
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

    @validator("release_date")
    def transform_date(cls, data: date):
        return data.isoformat()


class POSTBookInput(BaseModel):
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str

    @validator("release_date")
    def transform_date(cls, data: date):
        return data.isoformat()


class POSTBookOutput(BaseModel):
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str

    @validator("release_date")
    def transform_date(cls, data: date):
        return data.isoformat()
