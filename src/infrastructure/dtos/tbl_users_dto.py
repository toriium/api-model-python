from datetime import date

from pydantic import BaseModel


class TblUsersDTO(BaseModel):
    id: int
    username: str
    name: str
    password: str
    creation_date: date

    class Config:
        orm_mode = True


class CreateUserDTO(BaseModel):
    username: str
    name: str
    password: str
    creation_date: date
