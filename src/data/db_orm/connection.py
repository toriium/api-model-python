from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.settings import DatabaseEnv


def get_reading_db_url() -> str:
	# ------------- SQLITE -------------
	# url = 'sqlite:///teste.db'
	# url = URL.create(
	#     drivername="sqlite",
	#     database="example.db"
	# )

	# ------------- POSTGRESQL -------------
	url = f"postgresql+psycopg2://{DatabaseEnv.DB_USER}:{DatabaseEnv.DB_PASSWORD}@{DatabaseEnv.DB_HOST}:{DatabaseEnv.DB_PORT}/{DatabaseEnv.DB_NAME}"
	url = URL.create(
		drivername="postgresql+psycopg2",
		username=DatabaseEnv.DB_USER,
		password=DatabaseEnv.DB_PASSWORD,
		host=DatabaseEnv.DB_HOST,
		port=DatabaseEnv.DB_PORT,
		database=DatabaseEnv.DB_NAME,
	)

	# ------------- MYSQL -------------
	# url = f"mysql+mysqlconnector://{DatabaseEnv.DB_USER}:{DatabaseEnv.DB_PASSWORD}@{DatabaseEnv.DB_HOST}:{DatabaseEnv.DB_PORT}/{DatabaseEnv.DB_NAME}"
	# url = URL.create(drivername="mysql+mysqlconnector",
	#            username=DatabaseEnv.DB_USER,
	#            password=DatabaseEnv.DB_PASSWORD,
	#            host=DatabaseEnv.DB_HOST,
	#            port=DatabaseEnv.DB_PORT,
	#            database=DatabaseEnv.DB_NAME)

	return url.render_as_string(hide_password=False)


def get_writing_db_url() -> str:
	# ------------- SQLITE -------------
	# url = 'sqlite:///teste.db'
	# url = URL.create(
	#     drivername="sqlite",
	#     database="example.db"
	# )

	# ------------- POSTGRESQL -------------
	url = f"postgresql+psycopg2://{DatabaseEnv.DB_USER}:{DatabaseEnv.DB_PASSWORD}@{DatabaseEnv.DB_HOST}:{DatabaseEnv.DB_PORT}/{DatabaseEnv.DB_NAME}"
	url = URL.create(
		drivername="postgresql+psycopg2",
		username=DatabaseEnv.DB_USER,
		password=DatabaseEnv.DB_PASSWORD,
		host=DatabaseEnv.DB_HOST,
		port=DatabaseEnv.DB_PORT,
		database=DatabaseEnv.DB_NAME,
	)

	# ------------- MYSQL -------------
	# url = f"mysql+mysqlconnector://{DatabaseEnv.DB_USER}:{DatabaseEnv.DB_PASSWORD}@{DatabaseEnv.DB_HOST}:{DatabaseEnv.DB_PORT}/{DatabaseEnv.DB_NAME}"
	# url = URL.create(drivername="mysql+mysqlconnector",
	#            username=DatabaseEnv.DB_USER,
	#            password=DatabaseEnv.DB_PASSWORD,
	#            host=DatabaseEnv.DB_HOST,
	#            port=DatabaseEnv.DB_PORT,
	#            database=DatabaseEnv.DB_NAME)

	return url.render_as_string(hide_password=False)


# echo: logs every SQL statement issued through the engine, useful for debugging, keep False in production
# pool_size: number of persistent connections kept open per engine
# max_overflow: extra connections allowed on top of pool_size during load spikes
# pool_timeout: seconds to wait for a free connection before raising TimeoutError
# pool_recycle: recycle connections older than this (seconds), avoids using connections killed by the DB/network side
# pool_pre_ping: check connection liveness (SELECT 1) before handing it out, avoids "server closed the connection unexpectedly"
reading_engine = create_engine(
	url=get_reading_db_url(),
	echo=False,
	pool_size=5,
	max_overflow=10,
	pool_timeout=30,
	pool_recycle=1800,
	pool_pre_ping=True,
)
writing_engine = create_engine(
	url=get_writing_db_url(),
	echo=False,
	pool_size=5,
	max_overflow=10,
	pool_timeout=30,
	pool_recycle=1800,
	pool_pre_ping=True,
)

# class_: session class to instantiate (Session)
# autoflush: flush pending changes before each query (True)
# autocommit: legacy 1.x flag, keep False for explicit commit()/rollback()
# expire_on_commit: expire attributes after commit, forces fresh read next access (True)
# info: free-form dict on the session
ReadingSession = sessionmaker(
	bind=reading_engine,
	class_=Session,
	autoflush=True,
	autocommit=False,
	expire_on_commit=True,
	info=None,
)

WritingSession = sessionmaker(
	bind=writing_engine,
	class_=Session,
	autoflush=True,
	autocommit=False,
	expire_on_commit=True,
	info=None,
)
