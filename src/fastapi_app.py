from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.presentation.endpoints.book.book import book_router
from src.presentation.endpoints.books.books import books_router
from src.presentation.endpoints.health_check.health_check import health_check_router
from src.presentation.endpoints.token.token import token_router
from src.presentation.endpoints.user.user import user_router
from src.tracing import TempoMiddleware


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
    app.include_router(health_check_router)
    app.include_router(user_router)
    app.include_router(token_router)

    app.include_router(book_router)
    app.include_router(books_router)


def add_exception_handler(app: FastAPI):
    ...


def add_middleware(app: FastAPI):
    app.add_middleware(TempoMiddleware)
    origins = ["*"]
    app.add_middleware(CORSMiddleware,
                       allow_origins=origins,
                       allow_credentials=True,
                       allow_methods=["*"],
                       allow_headers=["*"], )


def get_fastapi_app() -> FastAPI:
    app = create_fastapi_app()
    add_middleware(app=app)
    add_exception_handler(app=app)
    add_router(app=app)

    return app
