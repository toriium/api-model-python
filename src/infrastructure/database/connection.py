from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.settings import DatabaseEnv

# url = 'sqlite:///teste.db'
url = f"mysql+mysqlconnector://{DatabaseEnv.DB_USER}:{DatabaseEnv.DB_PASSWORD}@{DatabaseEnv.DB_HOST}:{DatabaseEnv.DB_PORT}/{DatabaseEnv.DB_NAME}"
engine = create_engine(url, echo=False)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     expire_on_commit=False,
#     bind=engine
# )

SessionLocal = sessionmaker(
    bind=engine,
    class_=Session,
    autoflush=True,
    autocommit=False,
    expire_on_commit=True,
    info=None,
)
