from typing import Union

from src.infrastructure.errors.sql_error import SQLError


RepositoryError = Union[SQLError]