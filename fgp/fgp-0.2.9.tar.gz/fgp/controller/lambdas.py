from .client import Client
from fgp.utils.datetime_to_ms import datetime_to_ms
import datetime
import json
from typing import List, Tuple


class Lambdas:

    _client: Client = None

    def __init__(self, client: Client):
        self._client = client

    def call(
            self,
            device_type: str,
            lookup_key: str,
            lambda_name: str,
            payload: dict = None,
            lookup_name: str = 'name'
    ) -> dict:
        _payload = {
          "data": {"data": json.dumps(payload, sort_keys=True) if payload is not None else None }
        }
        res = self._client.post(route=f'{device_type}/{lookup_name}/{lookup_key}/{lambda_name}', data=_payload)
        if "response" in res:
            ret = res['response']
            try:
                return json.loads(ret)
            except Exception as e:
                raise Exception(f'Invalid response from lambda - could not parse as JSON - {e}')
        raise Exception(f'Inavlid response from lambda - does not contain "response" key - {res}')

    def call_many(
        self,
        device_type: str,
        lambda_name: str,
        lookup_name: str,
        payload: List[Tuple[str, dict]],
        timeout: str='30s',
    ):
        _payload = {
            "keyType": lookup_name,
            "timeout": timeout,
            "data": {
                key: {"data": json.dumps(value)} for key, value in payload
            }
        }
        result = self._client.post(route=f'{device_type}/{lambda_name}', data=_payload)

        return result
        # if "response" in res:
        #     ret = res['response']
        #     try:
        #         return json.loads(ret)
        #     except Exception as e:
        #         raise Exception(f'Invalid response from lambda - could not parse as JSON - {e}')
        # raise Exception(f'Inavlid response from lambda - does not contain "response" key - {res}')

