from datetime import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    name: str
    password: str
    creation_date: datetime

    class Config:
        from_attributes = True
