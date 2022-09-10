from pydantic import BaseModel
from datetime import datetime


class GetBookOutput(BaseModel):
    id: int
    isbn: str
    name: str
    author: str
    publisher: str
    release_date: datetime
    pages: int
    description: str
