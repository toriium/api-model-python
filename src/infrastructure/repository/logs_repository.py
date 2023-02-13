from src.infrastructure.db_orm.query_obj import insert_obj
from src.infrastructure.db_orm.tables import TblLogs


class LogsRepository:
    @staticmethod
    def create_log(log_message: str) -> None:
        log_obg = TblLogs()
        log_obg.log_message = log_message

        query_result, error = insert_obj(log_obg)
        if error:
            print(error)
