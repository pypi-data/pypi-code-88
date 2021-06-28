import requests
from typing import List


def batch(iterable, n=2500):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


def post_api_header(access_token):
    return {"Content-Type": "application/json", "Authorization": f'Bearer {access_token}'}


def get_api_header(access_token):
    return {"Authorization": f'Bearer {access_token}'}


def post(api_endpoint, json_params, access_token):
    verify = "localhost" not in api_endpoint
    return requests.post(url=api_endpoint, json=json_params, headers=post_api_header((access_token)), verify=verify)


def put(api_endpoint, json_params, access_token):
    verify = "localhost" not in api_endpoint
    return requests.put(url=api_endpoint, json=json_params, headers=post_api_header((access_token)), verify=verify)


def get(api_endpoint, access_token):
    verify = "localhost" not in api_endpoint
    return requests.get(url=api_endpoint, headers=get_api_header((access_token)), verify=verify)


def construct_event(commonUserId, event_id, event_type, kind, properties, timestamp=None, source_system_id=None):
    return {
        'commonUserId': commonUserId,
        'eventId': event_id,
        'eventType': event_type,
        'kind': kind,
        'properties': properties,
        'timestamp': timestamp,
        'sourceSystemId': source_system_id,
    }


def construct_user(commonUserId: str, name: str = None, properties: dict = None, integratedSystemId: int = None, userId: str = None):
    model = {
        'commonUserId': commonUserId,
        'name': name,
        'properties': properties,
    }
    if(integratedSystemId is not None):
        assert userId is not None
        model['integratedSystemReference'] = {
            'integratedSystemId': integratedSystemId,
            'userId': str(userId) # must be a string
        }

    return model
