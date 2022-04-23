import os
import sys
import uvicorn
from fastapi import FastAPI, APIRouter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application.routes.consult import consult_router
from application.routes.integrate import integrate_router
from application.routes.integrate_all import integrate_all_router
from application.routes.auth import auth_router

from application.database.init_db import create_database
from application.database.populate_db import populate_db

app = FastAPI()
router = APIRouter()

create_database()
populate_db()

app.include_router(consult_router)
app.include_router(integrate_router)
app.include_router(integrate_all_router)
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
