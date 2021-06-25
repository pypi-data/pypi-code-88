from typing import List, Dict
from .client import Client
from fgp.model.model import FGModel
from fgp.utils.datetime_to_ms import datetime_to_ms
import urllib.parse
import datetime


class Device:

    _client: Client = None

    def __init__(self, client: Client):
        self._client = client

    def get_many(
            self,
            device_type: str,
            device_names: str,
            extension_names: List[str]
    ) -> dict:
        data = {
            'devices': device_names,
            'extensions': extension_names
        }
        res = self._client.post(route=f'{device_type}', data=data)
        if len(res) == 0:
            return None
        return res

    # def get_schema(self, extension_name) -> FGModel:
    #     data = self._client.get(route=f'{reference_name}')
    #     return FGModel.from_object(reference_name, data.get('links', {}).get('persistenceInfo', []))

