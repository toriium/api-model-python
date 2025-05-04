from datetime import datetime

from pydantic import BaseModel


class TblBase(BaseModel):
    id: int | None = None
    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True