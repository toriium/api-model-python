import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uvicorn

from src.settings import FastAPIEnv
from src.infrastructure.db_orm.init_db import init_database
from src.fastapi_app import get_fastapi_app
from src.infrastructure.db_orm.populate_db import populate_db


def create_db():
    init_database()
    populate_db()


if __name__ == '__main__':
    create_db()
    app = get_fastapi_app()
    uvicorn.run(
        app=app,
        host=FastAPIEnv.APP_HOST,
        port=FastAPIEnv.APP_PORT,
        debug=False,
        log_level='info',
        access_log=True,
        workers=FastAPIEnv.APP_WORKERS,
        timeout_keep_alive=100
    )
