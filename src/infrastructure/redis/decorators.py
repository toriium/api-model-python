import pickle
from functools import wraps
from typing import Type

from src.infrastructure.redis.cache_expiration import CacheExpiration
from src.infrastructure.redis.redis_utils import RedisUtils


def verify_kwargs(kwargs):
    if not len(kwargs):
        raise ValueError("Pass values as kwargs")


def get_cached_value_1_return(key: str, expiration: int = CacheExpiration.ONE_HOUR) -> Type["Response"]:
    def handler_func(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            verify_kwargs(kwargs)

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


def get_cached_value_2_returns(key: str, expiration: int = CacheExpiration.ONE_HOUR) -> Type["Response"]:
    def handler_func(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            verify_kwargs(kwargs)

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


def set_cached_value_2_returns(key: str, expiration: int = CacheExpiration.ONE_HOUR) -> Type["Response"]:
    def handler_func(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            verify_kwargs(kwargs)

            formated_key = key.format_map(kwargs)

            func_return = function(*args, **kwargs)
            f_value, f_error = func_return

            if f_value and not f_error:
                serialized_value = pickle.dumps(f_value)
                RedisUtils.set(key_name=formated_key, key_value=serialized_value, expiration=expiration)

            return func_return

        return wrapper

    return handler_func


def delete_cached_value(key: str) -> Type["Response"]:
    def handler_func(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            verify_kwargs(kwargs)

            formated_key = key.format_map(kwargs)

            RedisUtils.delete(key_name=formated_key)

            func_return = function(*args, **kwargs)

            return func_return

        return wrapper

    return handler_func
