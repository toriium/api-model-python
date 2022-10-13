from datetime import datetime

from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    name: str
    password: str
    creation_date: datetime

    class Config:
        orm_mode = True


class CreateUserDTO(BaseModel):
    username: str
    name: str
    password: str
    creation_date: datetime
