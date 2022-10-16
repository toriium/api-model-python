import uuid
from src.infrastructure.redis.redis_utils import RedisUtils


class CacheTime:
    ONE_HOUR = 60 * 60


class TokenService:
    @staticmethod
    def token_is_valid(token: str) -> bool:
        return RedisUtils.exists(key_name=token)

    @staticmethod
    def create_token() -> str:
        new_token = f"token-{uuid.uuid4()}"
        expiration = CacheTime.ONE_HOUR

        RedisUtils.set(key_name=new_token, key_value='', expiration=expiration)

        return new_token

    @staticmethod
    def delete_token(token: str) -> None:
        RedisUtils.delete(key_name=token)

    @staticmethod
    def update_token_expiration(token: str) -> None:
        expiration = CacheTime.ONE_HOUR
        RedisUtils.expire(key_name=token, time=expiration)
