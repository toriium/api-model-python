from __future__ import annotations

from typing import Union
from datetime import timedelta

from src.infrastructure.errors.redis_error import RedisError
from src.infrastructure.redis.client import get_client


class RedisRepository:
    @staticmethod
    def set(key_name: str, key_value: str, expiration: int) -> None:
        """Set the string value of a key"""
        with get_client() as client:
            client.set(
                name=key_name,
                value=key_value,
                ex=expiration
            )

    @staticmethod
    def get(key_name: str) -> tuple[Union[str, None], Union[RedisError, None]]:
        """Get the value of key"""
        with get_client() as client:
            response = client.get(name=key_name)
            if response is None:
                return None, RedisError.nonexistent_key

            return response, None

    @staticmethod
    def expire(key_name: str, time: int | timedelta) -> None:
        """Changes ttl of a key"""
        with get_client() as client:
            client.expire(name=key_name, time=time)

    @staticmethod
    def persist(key_name: str) -> bool:
        """Remove the existing timeout on key"""
        with get_client() as client:
            response = client.persist(name=key_name)
            return True if response == 1 else False

    @staticmethod
    def ttl(key_name: str) -> tuple[Union[int, None], Union[RedisError, None]]:
        """Returns time to live in seconds of a key"""
        with get_client() as client:
            ttl = client.ttl(key_name)
            if ttl == -2:
                return None, RedisError.nonexistent_key
            elif ttl == -1:
                return None, RedisError.key_without_expiration
            else:
                return ttl, None

    @staticmethod
    def delete(key_name: str) -> None:
        """Delete a key"""
        with get_client() as client:
            client.delete(key_name)

    @staticmethod
    def flushdb() -> None:
        """Delete all the keys of the currently selected DB"""
        with get_client() as client:
            client.flushdb()

    @staticmethod
    def flushall() -> None:
        """Delete all the keys of all the existing databases, not just the currently selected one"""
        with get_client() as client:
            client.flushall()

    @staticmethod
    def key_exists(key_name: str) -> bool:
        """Veryfi if a key exists"""
        with get_client() as client:
            exists = client.exists(key_name)
            if exists:
                return True
            else:
                return False
