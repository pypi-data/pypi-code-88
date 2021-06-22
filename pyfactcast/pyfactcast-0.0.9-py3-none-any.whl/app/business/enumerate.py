from typing import List

from pyfactcast.client.sync import FactStore


def namespaces(*, fact_store: FactStore = FactStore()) -> List[str]:
    with fact_store as fs:
        return fs.enumerate_namespaces()


def types(namespace: str, *, fact_store: FactStore = FactStore()) -> List[str]:
    with fact_store as fs:
        return fs.enumerate_types(namespace)
