from datetime import date

from pydantic import BaseModel


class BookDomain(BaseModel):
    id: int = None
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: date
    pages: int
    description: str
