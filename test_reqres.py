from pprint import pprint

import requests
from pytest_voluptuous import S
from requests import Response
from voluptuous import Schema, PREVENT_EXTRA, Required, Optional, ALLOW_EXTRA


def test_get_users():
    result: Response = requests.get(
        "https://reqres.in/api/users",
        params={"page": 2}
    )
    # print(response.status_code)
    pprint(result.request.headers)
    assert result.status_code == 200
    assert result.json()['page'] == 2
    assert len(result.json()['data']) != 0


def test_create_user():
    name = "morpheus_2"
    job = "leader"

    result = requests.post(
        url="https://reqres.in/api/users",
        json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)


create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


def test_create_user_schema():
    name = "morpheus_2"
    job = "leader"

    result = requests.post(
        url="https://reqres.in/api/users",
        json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(create_user_schema)


put_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


def test_put_user_schema():
    name = "morpheus_23"
    job = "teamleader"

    result = requests.put(
        url="https://reqres.in/api/users/2",
        json={"name": name, "job": job}
    )

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(put_user_schema)


def test_delete_user():
    result = requests.delete(
        url="https://reqres.in/api/users/2",
    )
    assert result.status_code == 204


login_user_schema = Schema(
    {
        "token": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


def test_login_user_schema():
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    result = requests.post(
        url="https://reqres.in/api/login",
        json={"email": email, "password": password}
    )

    assert result.status_code == 200
    assert result.json() == S(login_user_schema)
