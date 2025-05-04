FROM python:3.11-slim-buster

# Creates a new patth called app
WORKDIR /var/www/app

# Copy all files to current dir
COPY . .

# Install python requirements
RUN pip install -r requirements.txt

# Add current path to PYTHONPATH
ENV PYTHONPATH "${PYTHONPATH}:/var/www/app"

# RUN
CMD ["opentelemetry-instrument", "python", "src/main.py" ]
