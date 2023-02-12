from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.settings import DatabaseEnv


def get_db_url():
    # url = 'sqlite:///teste.db'
    url = f"mysql+mysqlconnector://{DatabaseEnv.DB_USER}:{DatabaseEnv.DB_PASSWORD}@{DatabaseEnv.DB_HOST}:{DatabaseEnv.DB_PORT}/{DatabaseEnv.DB_NAME}"
    return url

engine = create_engine(get_db_url(), echo=False)


SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    autoflush=True,  # Takes updated object data from database
    autocommit=False,
    expire_on_commit=True,  # Remove object instance info
    info=None,
)
