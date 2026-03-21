from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TblBase(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int | None = None
	created_at: datetime
	updated_at: datetime
