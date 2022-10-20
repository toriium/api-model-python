from src.infrastructure.redis.redis_utils import RedisUtils


class TokensRepository:
    @staticmethod
    def token_is_valid(token: str) -> bool:
        return RedisUtils.exists(key_name=token)

    @staticmethod
    def create_token(new_token: str, expiration: int) -> None:
        RedisUtils.set(key_name=new_token, key_value='', expiration=expiration)

    @staticmethod
    def delete_token(token: str) -> None:
        RedisUtils.delete(key_name=token)

    @staticmethod
    def update_token_expiration(token: str, expiration) -> None:
        RedisUtils.expire(key_name=token, time=expiration)
