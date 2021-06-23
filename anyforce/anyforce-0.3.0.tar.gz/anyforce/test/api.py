import logging
from functools import cached_property
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, cast

from faker import Faker
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from anyforce import request

logger = logging.getLogger()


class TestAPI:
    @staticmethod
    def compare(lv: Any, rv: Any):
        if isinstance(lv, dict) and isinstance(rv, dict):
            lv = cast(Dict[str, Any], lv)
            rv = cast(Dict[str, Any], rv)
            for k, v in rv.items():
                if not TestAPI.compare(lv.get(k), v):
                    return False
            return True
        if isinstance(lv, list) and isinstance(rv, list):
            rv = cast(List[Any], rv)
            for i, v in enumerate(rv):
                if not TestAPI.compare(lv[i], v):
                    return False
            return True
        return lv == rv

    @property
    def endpoint(self) -> str:
        raise NotImplementedError()

    @cached_property
    def faker(self) -> Faker:
        return Faker()

    @property
    def create_tests(
        self,
    ) -> Iterable[
        Tuple[
            Dict[str, Any],
            int,
            Optional[Callable[[Dict[str, Any], Any], None]],
        ]
    ]:
        raise NotImplementedError()

    def test_create(
        self, client: TestClient, database: bool, router: APIRouter
    ):
        assert router
        assert database
        objs: List[Any] = []
        for json, status_code, callback in self.create_tests:
            r = request.post(self.endpoint, json=json, session=client)
            if (
                status_code < 300
                and r.status_code >= 300
                or r.status_code != status_code
            ):
                logger.info(json)
                logger.info(r.status_code)
                logger.info(r.text)
            assert r.status_code == status_code
            obj = r.json_object()
            if status_code < 300:
                assert obj
                assert obj["id"]
                assert obj["created_at"]
                assert obj["updated_at"]
                for k, v in json.items():
                    lv = obj.get(k)
                    if not self.compare(lv, jsonable_encoder(v)):
                        logger.info(lv)
                        logger.info(v)
                        assert False
            callback and callback(json, obj)
            objs.append(obj)
        return objs

    @property
    def list_tests(
        self,
    ) -> Iterable[
        Tuple[
            Dict[str, Any],
            int,
            Optional[Callable[[Dict[str, Any], Any], None]],
        ]
    ]:
        raise NotImplementedError()

    def test_list(self, client: TestClient, database: bool, router: APIRouter):
        assert router
        assert database
        rs: List[Any] = []
        for params, status_code, callback in self.list_tests:
            r = request.get(self.endpoint, params=params, session=client)
            assert r.status_code == status_code
            r = r.json_object()
            if status_code < 300:
                assert r
                assert r["total"] > 0
                assert len(r["data"]) > 0 and len(r["data"]) < params.get(
                    "limit", 20
                )
                assert params.get("offset", 0) + len(r["data"]) <= r["total"]

                prefetch: Any = params.get("prefetch", [])
                prefetch = (
                    prefetch if isinstance(prefetch, list) else [prefetch]
                )
                for k in prefetch:
                    exist = False
                    for e in r["data"]:
                        if e.get(k):
                            exist = True
                            break
                    assert exist
            callback and callback(params, r)
            rs.append(r)
        return rs
