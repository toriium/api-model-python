from pydantic import BaseModel, validator
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

    @validator("release_date")
    def transform_date(cls, data: date):
        return data.isoformat()
