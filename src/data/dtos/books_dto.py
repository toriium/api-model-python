from datetime import date

from pydantic import BaseModel, ConfigDict


class BookDTO(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	isbn: str
	name: str
	author: str
	publisher: str
	release_date: date
	pages: int
	description: str
