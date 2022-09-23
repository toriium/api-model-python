from pydantic import BaseModel, validator
from datetime import datetime


class User(BaseModel):
    id: int = None
    username: str
    name: str = None
    password: str
    creation_date: datetime = None