from contextlib import contextmanager

from redis.client import Redis
import redis


@contextmanager
def get_client() -> Redis:
    try:
        client = redis.Redis(
            host='localhost',
            port=6379,
            db=0,
            password=None
        )
        yield client
    finally:
        client.close()
