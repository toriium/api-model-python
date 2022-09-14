from typing import Any, Union
from copy import copy
from contextlib import contextmanager

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.infrastructure.db_orm.connection import SessionLocal
from src.infrastructure.errors.sql_error import SQLError


@contextmanager
def create_session() -> Session:
    """
    Way - 1
    with create_session() as session:
        var = session.query(User).filter_by(id=2).first()
        print(var.name)
    ----------------------------------------------------
    Way - 2
    with create_session() as session:
        results = session.query(User).all()
        for row in results:
            print(row.name)
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def select_first_obj(obj_table, kw_filters: dict):
    """
    Way - 1
    var = select_first_obj(obj=User, kw_filters={"id": 1})
    print(var)
    """
    with create_session() as session:
        query_result = session.query(obj_table).filter_by(**kw_filters).first()

    return query_result if query_result else None


def select_all_obj(obj_table, kw_filters: dict):
    """
    Way - 1
    vars = select_all_obj(obj=User, kw_filters={"id": 1})
    for var in vars:
        print(var)
    """
    with create_session() as session:
        query_result = session.query(obj_table).filter_by(**kw_filters).all()

    return query_result if query_result else None


def insert_obj(obj) -> tuple[Any, Union[SQLError, None]]:
    """
    Way - 1
    obj_user = User(name='nietzsche', age=55)
    insert_obj(obj=obj_user)
    ----------------------------------------------------
    Way - 2
    obj_user = User()
    obj_user.name = 'platao'
    obj_user.age = 65
    insert_obj(obj=obj_user)
    """
    try:
        with create_session() as session:
            session.add(obj)
            session.flush()
            updated_obj_data = copy(obj)
            session.commit()
    except IntegrityError as error:
        is_duplicate_entry = "1062 (23000): Duplicate entry" in str(error.orig)
        if is_duplicate_entry:
            return None, SQLError.duplicate_entry
        else:
            raise Exception("IntegrityError SQL error")

    return updated_obj_data, None


def insert_all_obj(objs: list):
    """
    Way - 1
    obj_user1 = User(name='zenao', age=55)
    obj_user2 = User(name='diogenes', age=55)
    insert_all_obj(objs=[obj_user1, obj_user2])
    """
    with create_session() as session:
        session.add_all(objs)
        session.flush()
        updated_obj_data = copy(objs)
        session.commit()

    return updated_obj_data


def update_obj(obj_table, kw_filters: dict, obj_update):
    """
    Way - 1
    update_obj(obj=User, kw_filters={"id": 1}, obj_update={User.name: 'zabuza', User.age: 50})
    ----------------------------------------------------
    Way - 2
    update_dict = {}
    update_dict[User.name] = 'aristoteles'
    update_dict[User.age] = 48
    update_obj(obj=User, kw_filters={"id": 1}, obj_update=update_dict)
    """
    with create_session() as session:
        session.query(obj_table).filter_by(**kw_filters).update(obj_update)
        session.flush()
        updated_obj_data = copy(obj_update)
        session.commit()

    return updated_obj_data


def delete_obj(obj_table, kw_filters: dict) -> None:
    """
    Way - 1
    delete_obj(obj=User, kw_filters={"id": 1})
    """
    with create_session() as session:
        session.query(obj_table).filter_by(**kw_filters).delete()
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
