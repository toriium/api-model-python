import pickle
from functools import wraps
from typing import Type

from src.infrastructure.redis.redis_utils import RedisUtils
from src.infrastructure.redis.cache_expiration import CacheExpiration


def get_cache_1_return(key: str, expiration: int = CacheExpiration.ONE_HOUR) -> Type["Response"]:
    def handler_func(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not len(kwargs):
                raise ValueError("Pass values as kwargs")

            formated_key = key.format_map(kwargs)

            cached_value, _ = RedisUtils.get(formated_key)
            if cached_value:
                return pickle.loads(cached_value), None

            func_return = function(*args, **kwargs)
            f_value = func_return

            if f_value:
                serialized_value = pickle.dumps(f_value)
                RedisUtils.set(key_name=formated_key, key_value=serialized_value, expiration=expiration)

            return func_return

        return wrapper

    return handler_func


def get_cache_2_return(key: str, expiration: int = CacheExpiration.ONE_HOUR) -> Type["Response"]:
    def handler_func(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not len(kwargs):
                raise ValueError("Pass values as kwargs")

            formated_key = key.format_map(kwargs)

            cached_value, _ = RedisUtils.get(formated_key)
            if cached_value:
                return pickle.loads(cached_value), None

            func_return = function(*args, **kwargs)
            f_value, f_error = func_return

            if f_value and not f_error:
                serialized_value = pickle.dumps(f_value)
                RedisUtils.set(key_name=formated_key, key_value=serialized_value, expiration=expiration)

            return func_return

        return wrapper

    return handler_func
