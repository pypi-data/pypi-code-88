import os
import requests
import json


API_URL_SUFFIX = 'coordinates'
ENABLED = os.environ.get('GEE_API_ENABLED', 'true') == 'true'
# make sure we are not using an old url
API_URL = f"{os.environ.get('GEE_API_URL', '').replace(API_URL_SUFFIX, '')}{API_URL_SUFFIX}"
API_KEY = os.getenv('GEE_API_KEY')
HEADERS = {
    'Content-Type': 'application/json',
    'X-Api-Key': API_KEY,
}


def is_enabled(): return ENABLED


def id_to_level(id: str): return id.count('.')


def fetch_data(**kwargs):
    try:
        data = json.dumps(kwargs)
        return requests.post(API_URL, data, headers=HEADERS).json().get('features', [])[0].get('properties')
    except Exception:
        return {}


def get_region_id(gid: str, **kwargs):
    # make sure we are not using an old url
    try:
        level = id_to_level(gid)
        field = f"GID_{level}"
        id = fetch_data(collection=f"users/hestiaplatform/gadm36_{level}",
                        ee_type='vector',
                        fields=field,
                        **kwargs
                        ).get(field)
        return None if id is None else f"GADM-{id}"
    except Exception:
        return None
