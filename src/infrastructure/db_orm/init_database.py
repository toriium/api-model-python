import time

from src.infrastructure.db_orm.connection import get_writing_db_url
from alembic.config import Config
from alembic import command
from src.settings import BASE_DIR


def init_database():
    time.sleep(10)
    path = f"{BASE_DIR}/src/infrastructure/db_orm/alembic"
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location",path)
    alembic_cfg.set_main_option("sqlalchemy.url", get_writing_db_url())

    command.upgrade(alembic_cfg, "head")
