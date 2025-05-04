FROM python:3.13.1-alpine3.21

# Creates a new patth called app
WORKDIR /var/www/app

# Copy all files to current dir
COPY . .

# Install python requirements
RUN pip install -r requirements.txt

# Add current path to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/var/www/app"

# RUN
# ENTRYPOINT ["opentelemetry-instrument", "python", "src/main.py"] 
ENTRYPOINT ["opentelemetry-instrument", "gunicorn", "src.main:app", "-c", "./src/gunicorn.conf.py"] 
