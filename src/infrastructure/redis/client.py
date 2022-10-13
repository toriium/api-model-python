from contextlib import contextmanager

from redis.client import Redis
import redis

from src.settings import RedisEnv


@contextmanager
def get_client() -> Redis:
    try:
        client = redis.Redis(
            host=RedisEnv.RE_HOST,
            port=RedisEnv.RE_PORT,
            db=0,
            password=None
        )
        yield client
    finally:
        client.close()
