from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from src.settings import ENV

# url = 'sqlite:///teste.db'
url = f"mysql+mysqlconnector://{ENV['DB_USER']}:{ENV['DB_PASSWORD']}@{ENV['DB_HOST']}:{ENV['DB_PORT']}/{ENV['DB_NAME']}"
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
