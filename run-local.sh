export OTEL_EXPORTER_OTLP_INSECURE=true
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
export OTEL_SERVICE_NAME=fastapi-service-automatic
export OTEL_PYTHON_LOG_CORRELATION=true
export OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true

#export PYTHONPATH="${PYTHONPATH}:$PWD" && poetry run opentelemetry-instrument uvicorn src.main:app --host 0.0.0.0 --port 8080 --workers 4
#export PYTHONPATH="${PYTHONPATH}:$PWD" && opentelemetry-instrument uvicorn src.main:app --host 0.0.0.0 --port 8080 --workers 4
export PYTHONPATH="${PYTHONPATH}:$PWD" && opentelemetry-instrument gunicorn src.main:app -c ./src/gunicorn_config.py
