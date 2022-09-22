import uuid
from src.infrastructure.repository.redis_repository import RedisRepository


class CacheTime:
    ONE_HOUR = 60 * 60


class TokenService:
    @staticmethod
    def token_is_valid(token: str) -> bool:
        return RedisRepository.key_exists(key_name=token)

    @staticmethod
    def create_token() -> str:
        new_token = f"token-{uuid.uuid4()}"
        expiration = CacheTime.ONE_HOUR

        RedisRepository.set(key_name=new_token, key_value='', expiration=expiration)

        return new_token
