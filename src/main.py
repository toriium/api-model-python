import uvicorn

from src.fastapi_app import get_fastapi_app
from src.infrastructure.db_orm.populate_db import populate_db
from src.settings import FastAPIEnv
from src.tracing import start_instrumentation


def create_db():
    # init_database()
    populate_db()


if __name__ == '__main__':
    create_db()
    app = get_fastapi_app()
    start_instrumentation(app=app)
    uvicorn.run(
        app=app,
        host=FastAPIEnv.APP_HOST,
        port=FastAPIEnv.APP_PORT,
        log_level='info',
        access_log=True,
        workers=FastAPIEnv.APP_WORKERS,
        timeout_keep_alive=100
    )
