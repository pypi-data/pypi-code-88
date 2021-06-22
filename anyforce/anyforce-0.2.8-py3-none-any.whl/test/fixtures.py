from typing import Iterable

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="session")
def app(models: Iterable[str]) -> FastAPI:
    initializer(models)
    return FastAPI()


@pytest.fixture(scope="session")
def client(app: FastAPI) -> TestClient:
    return TestClient(app)


@pytest.fixture(scope="module")
def database(models: Iterable[str]):
    initializer(models, db_url="sqlite://:memory:")
    yield True
    finalizer()
