import json
from typing import List

from aiohttp import ClientSession

from pyflipt import models

__all__ = ["get_client", "FliptClient", "FliptError"]


def safe_path_join(*url_parts) -> str:
    parts = []
    n_parts = len(url_parts)
    for index, part in enumerate(url_parts):
        if index == 0:
            parts.append(part.rstrip("/"))
        elif index == n_parts - 1:
            parts.append(part.lstrip("/"))
        else:
            parts.append(part.rstrip("/").lstrip("/"))
    return "/".join(parts)


CONFLICT_CODE = 3


class FliptError(Exception):
    def __init__(self, resp_json):
        self.resp_json = resp_json

    def __repr__(self):
        return f"FliptError({self.resp_json})"


class FliptClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = ClientSession()

    def get_url(self, unit: models.FliptBasicUnit) -> str:
        if isinstance(unit, models.Flag):
            url = safe_path_join(self.base_url, "/flags")
        elif isinstance(unit, models.Segment):
            url = safe_path_join(self.base_url, "/segments")
        elif isinstance(unit, models.Constraint):
            url = safe_path_join(
                self.base_url, f"/segments/{unit.segment_key}/constraints"
            )
        elif isinstance(unit, models.Rule):
            url = safe_path_join(self.base_url, f"/flags/{unit.flag_key}/rules")
        else:
            raise ValueError(f"Not supported yet {unit}")
        return url

    async def create(self, unit: models.FliptBasicUnit):
        url = self.get_url(unit)
        async with self.session.post(url, data=unit.json()) as resp:
            resp_json = await resp.json()
            if resp.status == 200:
                if isinstance(unit, models.Rule):
                    unit.id = resp_json["id"]
                return resp_json

            if resp.status == 400:
                if resp_json.get("code") == CONFLICT_CODE:
                    # Already there
                    return unit.dict()
            raise FliptError(resp_json)

    async def delete(self, unit: models.FliptBasicUnit):
        url = self.get_url(unit)
        async with self.session.delete(url) as resp:
            if resp.status == 404 or resp.status == 200:
                return
            else:
                resp_json = await resp.json()
                raise FliptError(resp_json)

    async def order_rules(self, flag_key: str, rule_ids: List[str]):
        url = safe_path_join(self.base_url, f"/flags/{flag_key}/rules/order")
        async with self.session.put(
            url, data=json.dumps({"flag_key": flag_key, "rule_ids": rule_ids})
        ) as resp:
            if resp.status != 200:
                resp_json = await resp.json()
                raise FliptError(resp_json)

    async def close(self):
        if not self.session.closed:
            await self.session.close()


def get_client(base_url) -> FliptClient:
    return FliptClient(base_url)
