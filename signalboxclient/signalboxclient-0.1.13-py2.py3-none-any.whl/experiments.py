from .client_functions import get, post
from .pagination import pageQuery, PaginatedResponse
from .exceptions import SignalBoxException


def create_experiment(access_token: str, base_url: str, offer_ids: list, name: str, concurrent_offers: int = 1, segment_id: str = None):
    json_params = {
        "offerIds": offer_ids,
        "segmentId": segment_id,
        "name": name,
        "concurrentOffers": concurrent_offers
    }
    r = post(f'{base_url}/api/experiments',
             json_params, access_token)
    if r.ok:
        return r.json()
    else:
        raise SignalBoxException(r.text)


def get_experiment(access_token: str, base_url: str, experiment_id: str):
    r = get(f'{base_url}/api/experiments/{experiment_id}', access_token)
    if r.ok:
        return r.json()
    else:
        raise SignalBoxException(r.text)


def query_experiments(access_token: str, base_url: str, page: int = None):
    r = get(f'{base_url}/api/experiments?{pageQuery(page)}', access_token)
    if r.ok:
        return PaginatedResponse(**r.json())
    else:
        raise SignalBoxException(r.text)


def get_offers_in_experiment(access_token: str, base_url: str, experiment_id: str):
    r = get(
        f'{base_url}/api/experiments/{experiment_id}/offers', access_token)
    if r.ok:
        return r.json()
    else:
        raise SignalBoxException(r.text)
