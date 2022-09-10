import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv('../env.env')

#
# class DatabaseEnv:
#     DB_HOST: str = os.getenv('DB_HOST')
#     DB_USER: str = os.getenv('DB_USER')
#     DB_PORT: str = os.getenv('DB_PORT')
#     DB_NAME: str = os.getenv('DB_NAME')
#     DB_PASSWORD: str = os.getenv('DB_PASSWORD')

class DatabaseEnv:
    DB_HOST: str = 'localhost'
    DB_USER: str = os.getenv('DB_USER')
    DB_PORT: str = os.getenv('DB_PORT')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
