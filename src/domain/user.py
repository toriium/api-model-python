from datetime import datetime

from pydantic import BaseModel


class UserDomain(BaseModel):
    id: int = None
    username: str
    name: str = None
    password: str
    creation_date: datetime = None
