from pydantic import BaseModel
from datetime import date


class Book(BaseModel):
    id: int = None
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str
