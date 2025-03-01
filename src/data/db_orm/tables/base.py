from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declarative_base

BaseDeclarative = declarative_base()


class Base(BaseDeclarative):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now, nullable=False)
    updated_at = Column(DateTime, server_default=func.now, server_onupdate=func.now, nullable=False)

    def model_to_dict(self) -> dict:
        # Convert the model instance to a dictionary, excluding internal attributes
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

    def columns(self):
        columns = self.__table__.columns.keys()
        return columns
