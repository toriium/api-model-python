from pydantic import ConfigDict

from src.data.dtos.tbl_base import TblBase


class UserDTO(TblBase):
	model_config = ConfigDict(from_attributes=True)

	username: str
	name: str
	password: str
