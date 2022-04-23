from contextlib import contextmanager

from sqlalchemy.orm import Session

from application.database.connection import SessionLocal
from application.database.models import Invalid


@contextmanager
def create_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def select_obj(obj, kw_filters: dict):
    with create_session() as session:
        resultado = session.query(obj).filter_by(**kw_filters).first()
        session.close()
        return resultado


def insert_obj(obj) -> None:
    with create_session() as session:
        session.add(obj)
        session.flush()
        session.commit()


def insert_all_obj(objs: list) -> None:
    with create_session() as session:
        session.add_all(objs)
        session.flush()
        session.commit()


def update_obj(obj, kw_filters: dict, obj_update) -> None:
    with create_session() as session:
        session.query(obj).filter_by(**kw_filters).update(obj_update)
        session.flush()
        session.commit()
        session.close()


def delete_obj(obj, kw_filters: dict) -> None:
    with create_session() as session:
        session.query(obj).filter_by(**kw_filters).delete()
        session.flush()
        session.commit()


if __name__ == '__main__':
    ...
    # ------------------------------------- use of create_session -------------------------------------
    # Form - 1
    # with create_session() as session:
    #     var = session.query(User).filter_by(id=2).first()
    #     print(var.name)

    # Form - 2
    # with create_session() as session:
    #     results = session.query(User).all()
    #     for row in results:
    #         print(row.name)

    # ------------------------------------- use of select_obj -------------------------------------
    # var = select_obj(obj=User, kw_filters={"id": 1})
    # print(var)

    # ------------------------------------- use of update_obj -------------------------------------
    # Form - 1
    # update_obj(obj=User, kw_filters={"id": 1}, obj_update={User.name: 'zabuza', User.age: 50})

    # Form - 2
    # update_dict = {}
    # update_dict[User.name] = 'aristoteles'
    # update_dict[User.age] = 48
    # update_obj(obj=User, kw_filters={"id": 1}, obj_update=update_dict)

    # ------------------------------------- use of insert_obj -------------------------------------
    # Form - 1
    # obj_user = User(name='nietzsche', age=55)
    # insert_obj(obj=obj_user)

    # Form - 2
    # obj_user = User()
    # obj_user.name = 'platao'
    # obj_user.age = 65
    # insert_obj(obj=obj_user)

    # ------------------------------------- use of insert_all_obj -------------------------------------
    # Form - 1
    # obj_user1 = User(name='zenao', age=55)
    # obj_user2 = User(name='diogenes', age=55)
    # insert_all_obj(objs=[obj_user1, obj_user2])

    # ------------------------------------- use of delete_obj -------------------------------------
    # delete_obj(obj=User, kw_filters={"id": 1})

    # ------------------------------------- use of SerializerMixin -------------------------------------
    # Form - 1
    # with create_session() as session:
    #     var = session.query(User).filter_by(id=2).first()
    #     print(var.to_dict())

    # Form - 2
    # with create_session() as session:
    #     results = session.query(User).all()
    #     results_dict = [result.to_dict() for result in results]
    #     print(results_dict)
