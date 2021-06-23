from datetime import datetime

import pytest

from sat.exceptions import RequestException


class FakeLogin:
    created = datetime.fromisoformat("2019-08-01 03:38:19.000")
    expires = datetime.fromisoformat("2019-08-01 03:43:19.000")
    uuid = "uuid-cf6c80fb-00ae-44c0-af56-54ec65decbaa-1"


@pytest.fixture
def test_login(login_handler):
    login_handler.login()


def test_reuse_token(login_handler):
    login_handler.login()
    first_token = login_handler.token
    login_handler.login()
    second_token = login_handler.token
    assert first_token == second_token


def test_login_expired(login_handler):
    with pytest.raises(RequestException):  # Expired session
        login_handler.login(
            created=FakeLogin.created,
            expires=FakeLogin.expires,
            uuid=FakeLogin.uuid,
        )
