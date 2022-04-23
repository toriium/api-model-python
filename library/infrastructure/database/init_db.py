import traceback
from time import sleep

from application.database.connection import engine
from application.database.models import Base


def create_database():
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
    create_database()
