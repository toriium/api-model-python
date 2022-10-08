from src.infrastructure.repository.logs_repository import LogsRepository


class LogService:
    @staticmethod
    def create_log(log_message: str):
        LogsRepository.create_log(log_message=log_message)
