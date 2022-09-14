from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text, Boolean, Date
from sqlalchemy_serializer import SerializerMixin

from src.infrastructure.db_orm.base import Base


class TblLogs(Base, SerializerMixin):
    __tablename__ = 'tbl_logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    log_message = Column(Text(), nullable=False)
    log_date = Column(TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return str(self.to_dict())
