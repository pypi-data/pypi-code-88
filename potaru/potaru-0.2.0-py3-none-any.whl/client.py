import requests
import json

_url = None
_token = None


def init(url: str = None, token: str = None):
    global _token
    global _url
    _url = url
    _token = token


def save(data: dict, **kwargs):
    requests.post(
        f"{_url}/v1/save", 
        headers={"Authorization": f"Bearer {_token}"},
        data={
            "tags": json.dumps(kwargs),
            "data": json.dumps(data),
        }
    )


def load(**kwargs):
    return requests.post(
        f"{_url}/v1/load", 
        headers={"Authorization": f"Bearer {_token}"},
        data=json.dumps(kwargs)
    ).json()["data"]
