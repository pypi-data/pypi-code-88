import os
import requests
from os import getenv
from pathlib import Path
from .errors import ApiKeyError
from .statics import API_BASE_URL, ENV_VAR_API_KEY, ENV_VAR_BASE_URL
from . import logger


API_KEY_LENGTH = 42


def get_api_base_url() -> str:
    return getenv(ENV_VAR_BASE_URL, '').strip() or API_BASE_URL


def get_api_key() -> str:
    api_key = getenv(ENV_VAR_API_KEY, '').strip()
    if not api_key:
        raise ApiKeyError(
            f"API key not found: ensure it is located in the {ENV_VAR_API_KEY} environment variable")
    if len(api_key) != API_KEY_LENGTH:
        raise ApiKeyError(f"API key has incorrect length, given: {api_key}")
    return api_key


def set_api_key(api_key) -> None:
    os.environ[ENV_VAR_API_KEY] = api_key


def set_log_level(level) -> None:
    logger.setLevel(level)


def download_image(url: str, destination: Path, overwrite=False):
    if destination.exists() and not overwrite:
        return
    remote_file = requests.get(url)
    destination.write_bytes(remote_file.content)
    # with open(destination, 'wb') as file:
    #     file.write(remote_file.content)
