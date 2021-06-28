from .client_functions import batch, get, post, put
from .pagination import pageQuery, PaginatedResponse
from .exceptions import SignalBoxException


def create_user(access_token, base_url: str, name: str, common_user_id: str):
    json_params = {
        "name": name,
        "commonUserId": common_user_id
    }
    r = post(f'{base_url}/api/trackedUsers',
             json_params, access_token)
    if r.ok:
        return r.json()
    else:
        raise SignalBoxException(r.text)


def create_or_update_users(access_token: str, base_url: str, users):
    for u in users:
        if 'commonUserId' not in u:
            raise Exception("Tracked Users require a commonUserId")
    results = []
    for u in batch(users):
        json_params = {
            "users": u
        }
        r = put(f'{base_url}/api/trackedUsers', json_params, access_token)
        if r.ok:
            results.append(r.json())
        else:
            raise SignalBoxException(r.text)
    return results
