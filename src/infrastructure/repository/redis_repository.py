import uuid

import redis

from src.infrastructure.redis.client import get_client


class RedisRepository:
    @staticmethod
    def set(key_name: str, key_value: str, expiration: int):
        with get_client() as client:
            client.set(
                name=key_name,
                value=key_value,
                ex=expiration
            )

    @staticmethod
    def get(key_name: str):
        with get_client() as client:
            value = client.get(name=key_name)
            return value

    @staticmethod
    def key_exists(key_name: str) -> bool:
        with get_client() as client:
            exists = client.exists(key_name)
            if exists:
                return True
            else:
                return False
