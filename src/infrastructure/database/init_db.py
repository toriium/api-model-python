import traceback
from time import sleep

from src.infrastructure.database.connection import engine
from src.infrastructure.database.base import Base


def init_database():
    for _ in range(10):
        sleep(10)
        try:
            Base.metadata.drop_all(bind=engine)
            Base.metadata.create_all(bind=engine)
            break
        except:
            traceback.print_exc()
            sleep(2)


if __name__ == '__main__':
    init_database()
