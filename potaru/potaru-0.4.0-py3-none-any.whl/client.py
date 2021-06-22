import requests
import json

_url = None
_token = None


def init(token: str = None, url: str = "https://potaru.io"):
    global _token
    global _url
    _url = url
    _token = token


def save(data: dict, **kwargs):
    response = requests.post(
        f"{_url}/v1/save", 
        headers={"Authorization": f"Bearer {_token}"},
        data=json.dumps({
            "tags": kwargs,
            "data": data,
        })
    )

    if 'error' in response:
        raise Exception(f"Failed to save data, error: {response['error']}")


# requests.post(f"https://potaru.io/v1/load", headers={"Authorization": f"Bearer 2095ea54083455a6c5a2bd0eb5c396784805df968d2a60d87df1888375ffd3af"}, data=json.dumps({}))

def load(**kwargs):
    response = requests.post(
        f"{_url}/v1/load", 
        headers={"Authorization": f"Bearer {_token}"},
        data=json.dumps(kwargs)
    ).json()

    if 'error' in response:
        if response['error'] == 'ITEM_NOT_FOUND':
            return None
        raise Exception(f"Failed to load data, error: {response['error']}")

    return response['data']
