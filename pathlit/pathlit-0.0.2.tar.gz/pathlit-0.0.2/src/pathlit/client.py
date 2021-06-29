import http.client
import json
from typing import TypedDict

PROD_HOST = "engine.pathlit.io"
weights_path = "/v1/optimiser/weights"
paths_path = "/v1/optimiser/paths"
sims_path = "/v1/optimiser/sims"


class DataPoint(TypedDict):
    date: str
    value: float


class TimeSeries(TypedDict):
    name: str
    data: list[DataPoint]


class Client:
    def __init__(self, api_key: str):
        self.header = {"x-api-key": api_key}
        self.host = PROD_HOST

    def get_weights(self, tickers: list[str]) -> dict[str, list[float]]:
        req_body = json.dumps({"tickers": tickers})
        s = self.__fetch(weights_path, req_body)
        res = json.loads(s)
        return res

    def get_paths(self, tickers: list[str]) -> list[TimeSeries]:
        req_body = json.dumps({"tickers": tickers})
        s = self.__fetch(paths_path, req_body)
        d = json.loads(s)

        return [parse_time_series(dc) for dc in d]

    def simulate(self, tickers: list[str], run_count=10) -> list[list[TimeSeries]]:
        req_body = json.dumps({"tickers": tickers, "run_count": run_count})
        resp_body = self.__fetch(sims_path, req_body)
        return parse_sims(resp_body)

    def __fetch(self, path: str, body: str) -> str:
        conn = http.client.HTTPSConnection(self.host)
        conn.request("POST", path, body, headers=self.header)
        s = conn.getresponse().read().decode()
        conn.close()
        return s


def parse_time_series(d: dict) -> TimeSeries:
    name = d["PATH"]
    res: TimeSeries = {"name": name, "data": []}
    for k, v in d.items():
        if k == "PATH":
            continue
        p: DataPoint = {"date": k, "value": float(v)}
        res["data"].append(p)
    return res


def parse_sims(input_str: str) -> list[list[TimeSeries]]:
    d = json.loads(input_str)
    res = []
    for i, run in d.items():
        res.append(list(map(lambda allocation: parse_time_series(allocation), run)))
    return res
