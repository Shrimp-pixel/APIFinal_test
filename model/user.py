import allure
import requests
from schemas.reqres_schemas import *
from pytest_voluptuous import S


class User:
    base_url = "https://reqres.in/api/users/"

    def __init__(self):
        self.result = None

    @allure.step('Базовая проверка успешности выполнения запроса')
    def check_basic(self, name, job, code):
        assert self.result.status_code == code

        data = self.result.json()
        assert data['name'] == name
        assert data['job'] == job

    @allure.step('Get user')
    def get_user(self, params):
        self.result = requests.get(
            url=f"{self.base_url}",
            params=params
        )
        return self.result

    @allure.step('Проверка get user')
    def check_get_user(self, params):
        assert self.result.status_code == 200

        for key, value in params.items():
            assert self.result.json()[key] == value

        assert len(self.result.json()['data']) != 0

    @allure.step('Post user')
    def create_user(self, name, job):
        self.result = requests.post(
            url=f"{self.base_url}",
            json={"name": name, "job": job}
        )
        return self.result

    @allure.step('Проверка post user')
    def check_create_user(self, name, job):
        self.check_basic(name, job, 201)
        assert isinstance(self.result.json()['id'], str)

    @allure.step('Проверка post user по схеме')
    def check_create_user_schema(self, name, job):
        self.check_create_user(name, job)
        assert self.result.json() == S(create_user_schema)

    @allure.step('Put user')
    def put_user(self, id_, name, job):
        self.result = requests.put(
            url=f"{self.base_url}{id_}/",
            json={"name": name, "job": job}
        )
        return self.result

    @allure.step('Проверка put user')
    def check_put_user(self, name, job):
        self.check_basic(name, job, 200)
        assert self.result.json() == S(put_user_schema)

    @allure.step('Delete user')
    def delete_user(self, id_):
        self.result = requests.delete(
            url=f"{self.base_url}{id_}/",
        )
        return self.result

    @allure.step('Проверка delete user')
    def check_delete_user(self):
        assert self.result.status_code == 204
