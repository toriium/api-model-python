from collections import OrderedDict
from contextlib import contextmanager

import mysql.connector
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursorDict
from pypika import Field, Query, Schema, Table

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
def get_cursor(connection: MySQLConnection) -> MySQLCursorDict:
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
    def query_all(query: str, params: list = None) -> list[dict]:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result if result else []

    @staticmethod
    def query_one(query: str, params: list = None) -> dict | None:
        with get_connection() as connection:
            with get_cursor(connection) as cursor:
                cursor.execute(query, params)
                result = cursor.fetchone()
                return result if result else None

    @staticmethod
    def create_insert_stm(schema, table: str, params: OrderedDict[str, any]) -> str:
        schema = Schema(schema)
        table = Table(table, schema=schema)

        stm = Query.into(table)
        stm = stm.columns(list(params.keys()))
        stm = stm.insert(list(params.values()))

        return stm.get_sql()

    @staticmethod
    def create_multiple_insert_stm(schema, table: str, params: list[OrderedDict[str, any]]) -> str:
        schema = Schema(schema)
        table = Table(table, schema=schema)

        stm = Query.into(table)
        stm = stm.columns(list(params[0].keys()))
        for param in params:
            stm = stm.insert(list(param.values()))

        return stm.get_sql()

    @staticmethod
    def create_update_stm(schema, table: str, params: dict[str, any], where_expressions: list | None = None) -> str:
        schema = Schema(schema)
        table = Table(table, schema=schema)

        stm = Query.update(table)
        for column, value in params.items():
            stm = stm.set(Field(column), value)

        if where_expressions:
            for where_expression in where_expressions:
                stm = stm.where(where_expression)

        return stm.get_sql()


if __name__ == '__main__':
    ...
