from .client_functions import get, post
from .exceptions import SignalBoxException


def create_touchpoint_on_tracked_user(access_token: str, base_url: str, tracked_user_id: str, touchpoint_id: str, values: dict, useInternalId: bool = None):
    json_params = {
        "values": values,
    }
    r = post(f'{base_url}/api/trackedUsers/{tracked_user_id}/touchpoints/{touchpoint_id}?useInternalId={useInternalId or ""}',
             json_params, access_token)
    if r.ok:
        return r.json()
    else:
        raise SignalBoxException(r.text)


def get_touchpoint_on_tracked_user(access_token: str, base_url: str, tracked_user_id: str, touchpoint_id: str, version: int = None, useInternalId: bool = None):
    r = get(f'{base_url}/api/trackedUsers/{tracked_user_id}/touchpoints/{touchpoint_id}?version={version or ""}&useInternalId={useInternalId or ""}', access_token)
    if r.ok:
        return r.json()
    else:
        raise SignalBoxException(r.text)
