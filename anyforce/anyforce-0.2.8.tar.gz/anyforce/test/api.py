from fastapi import APIRouter
from fastapi.testclient import TestClient

from anyforce import request


class TestAPI:
    @property
    def endpoint(self) -> str:
        raise NotImplementedError()

    def test_create(
        self, client: TestClient, database: bool, router: APIRouter
    ):
        assert router
        assert database
        r = request.post(self.endpoint, json={}, session=client)
        assert r.status_code < 300
        assert r.text
