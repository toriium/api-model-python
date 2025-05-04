import uvicorn

from src.data.db_orm.populate_db import populate_db
from src.data.db_orm.run_migration import run_migration
from src.fastapi_app import get_fastapi_app
from src.settings import FastAPIEnv


def create_db():
    run_migration()
    populate_db()


create_db()
app = get_fastapi_app()

if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=FastAPIEnv.APP_HOST,
        port=FastAPIEnv.APP_PORT,
        log_level='info',
        access_log=True,
        workers=FastAPIEnv.APP_WORKERS,
    )
