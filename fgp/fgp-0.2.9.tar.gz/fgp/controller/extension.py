from typing import List, Dict
from .client import Client
from fgp.model.model import FGModel
from fgp.utils.datetime_to_ms import datetime_to_ms
import urllib.parse
import datetime


class Extension:

    _client: Client = None

    def __init__(self, client: Client):
        self._client = client

    def get_at(
            self,
            device_type: str,
            device_name: str,
            extension_name: str,
            timestamp: datetime.datetime = None
    ) -> dict:
        data = {
            'devices': [device_name]
        }
        if timestamp:
            data['timestamp']: datetime_to_ms(timestamp)
        res = self._client.post(route=f'{device_type}/{extension_name}', data=data)
        if len(res) == 0:
            return None
        return res[0]
        return res

    def get_many(
            self,
            device_type: str,
            device_names: str,
            extension_name: str,
            timestamp: datetime.datetime = None
    ) -> dict:
        data = {
            'devices': device_names
        }
        if timestamp:
            data['timestamp']: datetime_to_ms(timestamp)
        res = self._client.post(route=f'{device_type}/{extension_name}', data=data)
        if len(res) == 0:
            return None
        return res[0]
        return res

    # def get_schema(self, extension_name) -> FGModel:
    #     data = self._client.get(route=f'{reference_name}')
    #     return FGModel.from_object(reference_name, data.get('links', {}).get('persistenceInfo', []))

