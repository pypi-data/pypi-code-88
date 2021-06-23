from typing import List

from sat.package import Package
from sat.query import Query
from sat.sat_connector import SATConnector


def test_query(query: Query):
    assert query.status == 5000


def test_verify(sat_connector: SATConnector, query: Query):
    query.verify(sat_connector)
    return query


def test_download(sat_connector: SATConnector, packages: List[Package]):
    for package in packages:
        package.download(sat_connector)
        with open(f"tests/downloads/{package.identifier}.zip", "wb") as f:
            f.write(package.binary)
