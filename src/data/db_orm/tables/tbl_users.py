from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_serializer import SerializerMixin

from src.data.db_orm.tables.base import Base


class TblUsers(Base, SerializerMixin):
	__tablename__ = "tbl_users"

	username: Mapped[str] = mapped_column(String(500), nullable=False, unique=True)
	name: Mapped[str] = mapped_column(Text(), nullable=False)
	password: Mapped[str] = mapped_column(Text(), nullable=False)

	def __repr__(self):
		return str(self.model_to_dict())
