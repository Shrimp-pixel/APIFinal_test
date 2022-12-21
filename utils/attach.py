import allure
from requests import Response


def add_body(response: Response):
    allure.attach(
        body=response.request.body,
        name='body request',
        attachment_type=allure.attachment_type.TEXT,
        extension='.txt',
    )
