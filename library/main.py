import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from library.views.books.book import book_router


def get_app():
    app = FastAPI()

    origins = ["*"]
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"], )

    app.include_router(book_router)
    return app


# create_database()
# populate_db()


if __name__ == '__main__':
    app = get_app()
    uvicorn.run(app, host="0.0.0.0", port=8080)
