# api-library

# Built With:

- [Python](https://www.python.org/) - Programming language
- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework
- [Pytest](https://docs.pytest.org/en/7.1.x/) - Test Framework
- [Allure](https://allurereport.org/) - Test Report UI
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
- [Alembic](https://github.com/sqlalchemy/alembic) - Database Migrations
- [PostgresSQL](https://www.postgresql.org/) - Database
- [Redis](https://redis.io/) - Cache
- [OpenTelemetry](https://opentelemetry.io/) - Telemetry
- [Grafana](https://grafana.com/) - Observaiblty
- [Tempo](https://grafana.com/oss/tempo/) - Traces
- [Prometheus](https://prometheus.io/) - Metrics
- [Loki](https://grafana.com/oss/loki/) - Logs
- [Ruff](https://github.com/charliermarsh/ruff) - Linter
- [Caddy](https://caddyserver.com/docs/) - Reverse Proxy Server

## System Requirements

- python ^3.11
- docker
- poetry

## How to run the app (Production)
```shell
  make run
```

## How to debug app
```shell
  make run_local
  python src/main.py
```

## How to run tests

### Install test tools
```shell
  sudo apt install inotify-tools
```

### Install Allure
```shell
  wget https://github.com/allure-framework/allure2/releases/download/2.33.0/allure_2.33.0-1_all.deb
  sudo dpkg -i allure_2.33.0-1_all.deb
```
### Test Commands
    1 - make run_dev
    2 - make test

## Layers
- domain: All main entities of the system
- application: All business logic
- data: All parts that interact with data, API, Cache, SQL, etc...
- presentation: How the system will be available, API, CLI, message-broker, etc...

# Notes
- It is using gunicorn because automatic instrumentations does not work with multi workers on uvicorn