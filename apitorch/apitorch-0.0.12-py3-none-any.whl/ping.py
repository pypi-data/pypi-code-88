from apitorch.api_client import Client
from apitorch.errors import ApitorchServerError, InvalidApiKey
from apitorch.routes import ping_route
from . import logger


def ping_api():
    logger.info('Request: Ping API')
    client = Client()
    response = client.get(ping_route())
    status_code = response.status_code
    if status_code != 200:
        return False
    return True
