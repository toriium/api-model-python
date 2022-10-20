import uuid
from src.infrastructure.repository.tokens_repository import TokensRepository


class CacheTime:
    ONE_HOUR = 60 * 60


class TokenService:
    @staticmethod
    def token_is_valid(token: str) -> bool:
        return TokensRepository.token_is_valid(token=token)

    @staticmethod
    def create_token() -> str:
        new_token = f"token-{uuid.uuid4()}"
        expiration = CacheTime.ONE_HOUR

        TokensRepository.create_token(new_token=new_token, expiration=expiration)

        return new_token

    @staticmethod
    def delete_token(token: str) -> None:
        TokensRepository.delete_token(token=token)

    @staticmethod
    def update_token_expiration(token: str) -> None:
        expiration = CacheTime.ONE_HOUR
        TokensRepository.update_token_expiration(token=token, expiration=expiration)
