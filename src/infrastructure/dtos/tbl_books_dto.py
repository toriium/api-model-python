from datetime import date

from pydantic import BaseModel


class BookDataDTO(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str

    class Config:
        orm_mode = True


class CreateUserDTO(BaseModel):
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str
