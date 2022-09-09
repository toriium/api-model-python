from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.endpoints.book.book import book_router


def create_fastapi_app() -> FastAPI:
    description = """
        # Library API

        ## Awsome Description
        - .... .. ... / .. ... / -. --- - / .- / -.. . ... -.-. .-. .. .--. - .. --- -. / .. -. / -- --- .-. ... . / -.-. --- -.. .
            """
    app = FastAPI(
        title="Library API",
        description=description,
        version="1.0",
        docs_url='/docs',
        redoc_url='/redoc'
    )

    return app


def add_router(app: FastAPI):
    app.include_router(book_router)


def add_middleware(app: FastAPI):
    origins = ["*"]
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"], )


def get_fastapi_app() -> FastAPI:
    app = create_fastapi_app()
    add_middleware(app=app)
    add_router(app=app)

    return app
