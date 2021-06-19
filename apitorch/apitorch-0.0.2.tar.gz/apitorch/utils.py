import os
from os import getenv
from .errors import ApiKeyError
from .statics import API_BASE_URL, ENV_VAR_API_KEY, ENV_VAR_BASE_URL


API_KEY_LENGTH = 42


def get_api_base_url():
    return getenv(ENV_VAR_BASE_URL, '') or API_BASE_URL


def get_api_key():
    api_key = getenv(ENV_VAR_API_KEY, '').strip()
    if not api_key:
        raise ApiKeyError(
            f"API key not found: ensure it is located in the {ENV_VAR_API_KEY} environment variable")
    if len(api_key) != API_KEY_LENGTH:
        raise ApiKeyError(f"API key has incorrect length, given: {api_key}")
    return api_key


def set_api_key(api_key):
    os.environ[ENV_VAR_API_KEY] = api_key
