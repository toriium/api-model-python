from sqlalchemy import TIMESTAMP, Column, Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy_serializer import SerializerMixin

from src.data.db_orm.tables.base import Base


class TblUsers(Base, SerializerMixin):
    __tablename__ = 'tbl_users'

    username = Column(String(500), nullable=False, unique=True)
    name = Column(Text(), nullable=False)
    password = Column(Text(), nullable=False)

    def __repr__(self):
        return str(self.to_dict())
