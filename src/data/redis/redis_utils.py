from __future__ import annotations

from datetime import timedelta

from src.data.errors.redis_error import RedisError
from src.data.redis.client import get_client


class RedisUtils:
    # -------------------------------------------------------------- #
    #                               GENERAL
    # -------------------------------------------------------------- #
    @staticmethod
    def set(key_name: str, key_value: [str, bytes], expiration: int | timedelta) -> None:
        """Set the string value of a key."""
        with get_client() as client:
            client.set(
                name=key_name,
                value=key_value,
                ex=expiration
            )

    @staticmethod
    def get(key_name: str) -> tuple[(str, bytes) | None, RedisError | None]:
        """Get the value of key."""
        with get_client() as client:
            response = client.get(name=key_name)
            if response is None:
                return None, RedisError.nonexistent_key

            return response, None

    @staticmethod
    def delete(key_name: str) -> None:
        """Delete a key."""
        with get_client() as client:
            client.delete(key_name)

    @staticmethod
    def exists(key_name: str) -> bool:
        """Veryfi if a key exists."""
        with get_client() as client:
            exists = client.exists(key_name)
            if exists:
                return True
            else:
                return False

    # -------------------------------------------------------------- #
    #                               TTL
    # -------------------------------------------------------------- #
    @staticmethod
    def expire(key_name: str, time: int | timedelta) -> None:
        """Change ttl of a key."""
        with get_client() as client:
            client.expire(name=key_name, time=time)

    @staticmethod
    def persist(key_name: str) -> bool:
        """Remove the existing timeout on key."""
        with get_client() as client:
            response = client.persist(name=key_name)
            return True if response == 1 else False

    @staticmethod
    def ttl(key_name: str) -> tuple[int | None, RedisError | None]:
        """Returns time to live in seconds of a key."""
        with get_client() as client:
            ttl = client.ttl(key_name)
            if ttl == -2:
                return None, RedisError.nonexistent_key
            elif ttl == -1:
                return None, RedisError.key_without_expiration
            else:
                return ttl, None

    # -------------------------------------------------------------- #
    #                               HASH
    # -------------------------------------------------------------- #
    @staticmethod
    def hset(hash_name: str, key_name: str, key_value: str) -> None:
        """Set the string value of a hash field."""
        with get_client() as client:
            client.hset(
                name=hash_name,
                key=key_name,
                value=key_value)

    @staticmethod
    def hget(hash_name: str, key_name: str) -> tuple[str | None, RedisError | None]:
        """Get the value of a hash field."""
        with get_client() as client:
            response = client.hget(name=hash_name, key=key_name)
            if response is None:
                return None, RedisError.nonexistent_key

            return response, None

    @staticmethod
    def hdel(hash_name: str, key_name: str) -> None:
        """Delete one or more filds in a hash."""
        with get_client() as client:
            client.hdel(hash_name, key_name)

    @staticmethod
    def hexists(hash_name: str, key_name: str) -> bool:
        """Determine if a hash field exists."""
        with get_client() as client:
            exists = client.hexists(name=hash_name, key=key_name)
            return exists

    # -------------------------------------------------------------- #
    #                               FLUSH
    # -------------------------------------------------------------- #
    @staticmethod
    def flushdb() -> None:
        """Delete all the keys of the currently selected DB."""
        with get_client() as client:
            client.flushdb()

    @staticmethod
    def flushall() -> None:
        """Delete all the keys of all the existing databases, not just the currently selected one."""
        with get_client() as client:
            client.flushall()
