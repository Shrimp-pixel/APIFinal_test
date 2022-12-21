import allure
import requests
from schemas.reqres_schemas import *
from pytest_voluptuous import S


class Login:
    base_url = "https://reqres.in/api/login/"

    def __init__(self):
        self.result = None
        self.auth_token = None

    @allure.step('Login user')
    def login_user(self, email, password):
        self.result = requests.post(
            url=f"{self.base_url}",
            json={"email": email, "password": password}
        )
        return self.result

    @allure.step('Проверка что user login')
    def check_login_user(self):
        assert self.result.status_code == 200

        auth_token = self.result.json()["token"]
        assert auth_token is not None
        self.auth_token = auth_token

        print(self.auth_token)

        assert self.result.json() == S(login_user_schema)
