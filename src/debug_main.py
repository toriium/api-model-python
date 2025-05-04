import os
import subprocess

# Set OTEL environment variables
os.environ["OTEL_EXPORTER_OTLP_ENDPOINT"] = "http://0.0.0.0:4317"
os.environ["OTEL_EXPORTER_OTLP_INSECURE"] = "true"
os.environ["OTEL_SERVICE_NAME"] = "fastapi-service"

# Call OpenTelemetry CLI wrapper
subprocess.run(["opentelemetry-instrument", "python", "src/main.py"])
