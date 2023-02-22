from contextlib import contextmanager

import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import CursorBase

from src.settings import DatabaseEnv


@contextmanager
def get_connection() -> MySQLConnection:
    conexao = mysql.connector.connect(
        host=DatabaseEnv.DB_HOST,
        user=DatabaseEnv.DB_USER,
        password=DatabaseEnv.DB_PASSWORD,
        port=DatabaseEnv.DB_PORT,
        db=DatabaseEnv.DB_NAME,
    )

    try:
        yield conexao
    finally:
        conexao.close()


@contextmanager
def get_cursor(connection: MySQLConnection) -> CursorBase:
    cursor = connection.cursor(dictionary=True, buffered=True)
    try:
        yield cursor
    finally:
        cursor.close()


class DBUtils:
    @staticmethod
    def execute(query: str, params: list = None) -> None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                connection.commit()

    @staticmethod
    def executemany(query: str, params: list[list] = None) -> None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.executemany(query, params)
                connection.commit()

    @staticmethod
    def consult_all(query: str, params: list = None) -> list[dict] | None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result if result else None

    @staticmethod
    def consult_one(query: str, params: list = None) -> dict | None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()
                return result if result else None


if __name__ == '__main__':
    ...
