from sqlalchemy import DateTime, Integer, func
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

BaseDeclarative = declarative_base()


class Base(BaseDeclarative):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(), server_onupdate=func.now(), nullable=False)

    def model_to_dict(self) -> dict:
        # Convert the model instance to a dictionary, excluding internal attributes
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

    def columns(self):
        columns = self.__table__.columns.keys()
        return columns
