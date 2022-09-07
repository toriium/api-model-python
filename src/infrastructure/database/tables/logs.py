from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text, Boolean, Date
from sqlalchemy_serializer import SerializerMixin

from src.infrastructure.database.base import Base


class Log(Base, SerializerMixin):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    logMessage = Column(Text(), nullable=False)
    logDate = Column(TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return str(self.to_dict())
