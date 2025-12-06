from sqlalchemy import Date, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_serializer import SerializerMixin

from src.data.db_orm.tables.base import Base


class TblBooks(Base, SerializerMixin):
    __tablename__ = 'tbl_books'

    isbn: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(500), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(200), nullable=False)
    publisher: Mapped[str] = mapped_column(String(500), nullable=False)
    release_date: Mapped[Date] = mapped_column(Date(), nullable=False)
    pages: Mapped[int] = mapped_column(Integer(), nullable=False)
    description: Mapped[str] = mapped_column(Text(), nullable=False)

    def __repr__(self):
        return str(self.model_to_dict())
