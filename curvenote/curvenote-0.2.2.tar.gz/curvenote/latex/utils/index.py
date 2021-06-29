import logging
import requests
from collections import namedtuple
from typing import NamedTuple
from ...models import BlockVersion


logger = logging.getLogger()

LocalReferenceItem = namedtuple(
    "LocalReferenceItem", ["block_path", "local_tag", "bibtex"]
)

class LocalMarker(NamedTuple):
    marker: str
    local_path: str
    remote_path: str


# TODO move to session - easier to mock
def get_model(session, url, model=BlockVersion):
    block = session._get_model(url, model)
    if not block:
        raise ValueError(f"Could not fetch the block {url}")
    return block


def fetch(url: str):
    resp = requests.get(url)
    if resp.status_code >= 400:
        raise ValueError(resp.content)
    return resp.content

