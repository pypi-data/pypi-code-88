import requests
from .errors import *

def api_bot_auth(token, url):
    if token == None:
        raise APIError("This function needs a bot token, please check the documentation! https://daw.readthedocs.io/")
    request = requests.get(url=url, headers={"Authorization": f"Bot {token}"})
    if request.status_code == 200:
        response = request.json()
        return response
    else:
        raise APIError(f"Something failed. Server response: {request.status_code}")

def api_user_auth(url, token):
    request = requests.get(url=url, headers={"Authorization": f"Bearer {token}"})
    if request.status_code == 200:
        response = request.json()
        return response
    else:
        raise APIError(f"Something failed. Server response: {request.status_code}")