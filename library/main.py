import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uvicorn
from fastapi import FastAPI, APIRouter

from library.views.books.book import book_router


def get_app():
    app = FastAPI()
    app.include_router(book_router)
    return app


# create_database()
# populate_db()


if __name__ == '__main__':
    app = get_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
