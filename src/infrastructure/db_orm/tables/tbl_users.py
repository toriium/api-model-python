from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text, Boolean, Date
from sqlalchemy_serializer import SerializerMixin

from src.infrastructure.db_orm.base import Base


class TblUsers(Base, SerializerMixin):
    __tablename__ = 'tbl_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(500), nullable=False, unique=True)
    name = Column(Text(), nullable=False)
    password = Column(Text(), nullable=False)
    creation_date = Column(Date(), nullable=False)

    def __repr__(self):
        return str(self.to_dict())
