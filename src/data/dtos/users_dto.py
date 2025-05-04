

from src.data.dtos.tbl_base import TblBase


class UserDTO(TblBase):
    username: str
    name: str
    password: str

    class Config:
        from_attributes = True
