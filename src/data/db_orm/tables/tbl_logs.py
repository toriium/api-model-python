from sqlalchemy import TIMESTAMP, Column, Text
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin

from src.data.db_orm.tables.base import Base


class TblLogs(Base, SerializerMixin):
    __tablename__ = 'tbl_logs'

    log_message = Column(Text(), nullable=False)
    log_date = Column(TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return str(self.to_dict())
