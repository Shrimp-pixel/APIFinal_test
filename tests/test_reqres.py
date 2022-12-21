from pprint import pprint

import allure
from allure_commons.types import Severity

from model.user import User
from model.login import Login


@allure.tag('api')
@allure.label(Severity.NORMAL)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка api reqres')
@allure.story("Получение users")
def test_get_users():
    params = {"page": 2}

    PObj = User()
    result = PObj.get_user(params)

    # print(response.status_code)
    pprint(result.request.headers)

    PObj.check_get_user(params)


@allure.tag('api')
@allure.label(Severity.NORMAL)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка api reqres')
@allure.story("Создание user")
def test_create_user():
    name = "morpheus_2"
    job = "leader"

    PObj = User()
    PObj.create_user(name, job)

    PObj.check_create_user(name, job)


@allure.tag('api')
@allure.label(Severity.NORMAL)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка api reqres')
@allure.story("Создание user и проверка по схеме")
def test_create_user_schema():
    name = "morpheus_2"
    job = "leader"

    PObj = User()
    PObj.create_user(name, job)

    PObj.check_create_user_schema(name, job)


@allure.tag('api')
@allure.label(Severity.NORMAL)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка api reqres')
@allure.story("Редактирование user и проверка по схеме")
def test_put_user_schema():
    name = "morpheus_23"
    job = "teamleader"
    id_ = 2

    PObj = User()
    PObj.put_user(id_, name, job)

    PObj.check_put_user(name, job)


@allure.tag('api')
@allure.label(Severity.NORMAL)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка api reqres')
@allure.story("Удаление user")
def test_delete_user():
    id_ = 2

    PObj = User()
    PObj.delete_user(id_)

    PObj.check_delete_user()


@allure.tag('api')
@allure.label(Severity.NORMAL)
@allure.label('owner', 'Shrimp-pixel')
@allure.feature('Проверка api reqres')
@allure.story("Login user")
def test_login_user_schema():
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    PObj = Login()
    PObj.login_user(email, password)

    PObj.check_login_user()
