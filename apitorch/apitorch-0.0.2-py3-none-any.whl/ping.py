from apitorch.api_client import Client
from apitorch.errors import ApitorchServerError, InvalidApiKey
from apitorch.routes import PING
from apitorch.utils import get_api_key
from requests import get
from . import logger


def ping_api(**args):
    client = Client()
    logger.debug('Ping API')
    response = client.get(PING)
    status_code = response.status_code

    if status_code == 200:
        return True

    if status_code == 401:
        raise InvalidApiKey(
            'Invalid API key. Repeat this call with a valid API key: https://www.apitorch.com/account')

    raise ApitorchServerError(
        f'A server error prevented this request from executing. status: {status_code}')
