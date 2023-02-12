from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, TIMESTAMP, Text
from sqlalchemy_serializer import SerializerMixin

from src.infrastructure.db_orm.tables.base import Base


class TblUsers(Base, SerializerMixin):
    __tablename__ = 'tbl_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(500), nullable=False, unique=True)
    name = Column(Text(), nullable=False)
    password = Column(Text(), nullable=False)
    creation_date = Column(TIMESTAMP(), nullable=False, server_default=func.now())

    def __repr__(self):
        return str(self.to_dict())
