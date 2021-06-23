from typing import Iterable
import ray


@ray.remote
def _http_remote(f, payload: dict):
    resp = f(**payload)
    return resp


def http_parallel(f, payloads: Iterable[dict]):
    if ray.is_initialized():
        ray.shutdown()
    ray.init()
    results = ray.get([_http_remote.remote(f, payload) for payload in payloads])
    ray.shutdown()
    return results
