import datetime

from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()


class Invalid(Base, SerializerMixin):
    __tablename__ = 'invalids'

    id = Column(Integer, primary_key=True, autoincrement=True)
    companyDocument = Column(String(200), nullable=False, unique=True)
    companyName = Column(String(200), nullable=False, unique=True)
    customerDocument = Column(String(12), nullable=False, unique=True)
    value = Column(Float())
    contract = Column(String(200))
    debtDate = Column(TIMESTAMP(timezone=True), server_default=func.now())
    inclusionDate = Column(TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return str(self.to_dict())


class Authorized(Base, SerializerMixin):
    __tablename__ = 'authorized'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(Text(), nullable=False)
    password = Column(Text(), nullable=False)
    active = Column(Boolean(), nullable=False, server_default='1')


class Log(Base, SerializerMixin):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    logMessage = Column(Text(), nullable=False)
    logDate = Column(TIMESTAMP(timezone=True), server_default=func.now())

    def __repr__(self):
        return str(self.to_dict())
