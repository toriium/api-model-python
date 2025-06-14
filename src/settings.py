import os
from pathlib import Path

from dotenv import find_dotenv, load_dotenv

if not os.getenv("PRD_ENV"):
    print("Loading local environment variables...")
    env_path = find_dotenv("../local.env")
    load_dotenv(env_path)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = str(Path(f"{BASE_DIR}/src/templates"))




class FastAPIEnv:
    APP_HOST: str = os.getenv("APP_HOST")
    APP_PORT: int = int(os.getenv("APP_PORT"))
    APP_WORKERS: int = int(os.getenv("APP_WORKERS"))


class TokenEnv:
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    REFRESH_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))

class DatabaseEnv:
    DB_HOST: str = os.getenv("DB_HOST")
    DB_USER: str = os.getenv("DB_USER")
    DB_PORT: int = int(os.getenv("DB_PORT"))
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")


class RedisEnv:
    RE_HOST: str = os.getenv("RE_HOST")
    RE_PORT: int = int(os.getenv("RE_PORT"))
