import os
import sys

from src.infrastructure.db_orm.init_db import init_database
from src.fastapi_app import get_fastapi_app
import uvicorn


# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def create_db():
    init_database()
    # populate_db()
    ...


if __name__ == '__main__':
    init_database()
    app = get_fastapi_app()
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8080,
        debug=False,
        log_level='info',
        access_log=True,
        workers=1,
        timeout_keep_alive=100
    )
