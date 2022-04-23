from application.database.utils import insert_obj
from application.database.models import Authorized
from application.cryptography.cryptography import Cryptography


def populate_db():
    obj_authorized = Authorized()
    obj_authorized.username = 'ultra_secret_user'
    obj_authorized.password = Cryptography.encrypt('ultra_secret_password')
    obj_authorized.active = 1

    insert_obj(obj=obj_authorized)
