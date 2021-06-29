import requests


def request(url, header=None, params=None, verify=None):
    return requests.get(url, headers=header, params=params, verify=verify)


def request_json(url, header=None, params=None, verify=None):
    response = request(url, header, params, verify)
    return response.json()
