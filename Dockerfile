FROM python:3.9-slim-buster
COPY ./requirements.txt /var/www/requirements.txt
WORKDIR /var/www
RUN pip install -r requirements.txt
COPY . /var/www
WORKDIR /var/www
ENV PYTHONPATH "${PYTHONPATH}:/var/www/src"
CMD [ "python", "src/main.py" ]
