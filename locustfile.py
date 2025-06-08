from faker import Faker
from locust import HttpUser, between, task

from src.presentation.schemas.user_schema import CreateUserInput


class QuickstartUser(HttpUser):
    wait_time = between(1, 10)

    @task()
    def home(self):
        self.client.get(url="/", name="/home")

    @task()
    def health_check(self):
        self.client.get(url="/health_check", name="/health_check")

    @task()
    def check_user(self):
        data = {"username": "john.doe", "password": "123"}
        self.client.get(url="/user", name="/user", data=data)

    @task()
    def create_user(self):
        fake = Faker()
        user = CreateUserInput(username=fake.name(), name=fake.name(), password=fake.text())
        data = user.model_dump()
        self.client.post(url="/user", name="/create_user", json=data)


# Usage: locust -f locustfile.py --headless --users 20 --spawn-rate 10 -H http://localhost:8080
