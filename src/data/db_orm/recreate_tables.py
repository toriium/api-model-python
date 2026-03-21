from time import sleep

from sqlalchemy import text

from src.data.db_orm.connection import writing_engine
from src.data.db_orm.tables.base import Base


def recreate_tables():
	for _ in range(10):
		try:
			# In case you wanna reset alembic versioning
			with writing_engine.connect() as conn:
				conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
				conn.commit()

			Base.metadata.drop_all(bind=writing_engine)
			Base.metadata.create_all(bind=writing_engine)
			break
		except Exception as error:
			print(error)
			sleep(2)


if __name__ == "__main__":
	recreate_tables()
