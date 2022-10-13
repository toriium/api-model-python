from src.infrastructure.db_orm.query_obj import create_session
from src.application.crypt.crypt_service import CryptService


def add_tbl_users() -> list:
    commands = [
        f"""insert into tbl_users (username, name, password) 
            values ('john.doe', 'john doe', '{CryptService.encrypt('123')}');""",
    ]
    return commands


def populate_db():
    with create_session() as session:
        commands = []
        commands.extend(add_tbl_users())

        for command in commands:
            session.execute(command)
        session.commit()
