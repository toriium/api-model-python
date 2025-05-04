from src.settings import FastAPIEnv

HOST = FastAPIEnv.APP_HOST
PORT = FastAPIEnv.APP_PORT
WORKERS = FastAPIEnv.APP_WORKERS

bind = f"{HOST}:{PORT}"
workers = WORKERS
worker_connections = 1000
max_requests = int(workers * worker_connections)
max_requests_jitter = 5
keepalive = 120
timeout = 120
worker_class = "uvicorn.workers.UvicornWorker"
# Preload the app before forking workers, solves auto intrumentation issue with multi workers on uvicorn
preload_app = True

# gunicorn src.main:app -c ./src/gunicorn.conf.py
