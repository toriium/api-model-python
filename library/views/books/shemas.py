from pydantic import BaseModel, validator
from datetime import datetime


class Message(BaseModel):
    message: str


class BookGetOutput(BaseModel):
    companyDocument: str
    companyName: str
    customerDocument: str
    value: float
    contract: str
    debtDate: datetime
    inclusionDate: datetime

    @validator("debtDate", 'inclusionDate')
    def datetime_to_string(cls, v):
        return v.isoformat()

    class Config:
        orm_mode = True
