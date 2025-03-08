# api-library

# Built With:

- [Python](https://www.python.org/) - Programming language
- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [Pytest](https://docs.pytest.org/en/7.1.x/) - Test Framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
- [Alembic](https://github.com/sqlalchemy/alembic) - Database Migrations
- [MySQL](https://www.mysql.com/) - Database
- [Redis](https://redis.io/) - Cache
- [OpenTelemetry](https://opentelemetry.io/) - Telemetry
- [Jaeger](https://www.jaegertracing.io/) - APM
- [Ruff](https://github.com/charliermarsh/ruff) - Linter

## System Requirements

- python ^3.11
- docker
- poetry

## How to run the application

    make run_local
    poetry run ./src/main.py

## How to run tests

    1 - make run_dev
    2 - make test

## Layers
- domain: All main entities of the system
- application: All business logic
- data: All parts that interact with data, API, Cache, SQL, etc...
- presentation: How the system will be available, API, CLI, message-broker, etc...