from datetime import date

from pydantic import BaseModel


class BookDTO(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str

    class Config:
        from_attributes = True
