from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text, Boolean, Date
from sqlalchemy_serializer import SerializerMixin

from src.infrastructure.database.base import Base


class Books(Base, SerializerMixin):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(20), nullable=False, unique=True)
    name = Column(String(500), nullable=False, unique=True)
    author = Column(String(200), nullable=False, unique=True)
    publisher = Column(String(500), nullable=False)
    release_date = Column(Date(), nullable=False)
    pages = Column(Integer(), nullable=False)
    description = Column(Text(), nullable=False)

    def __repr__(self):
        return str(self.to_dict())