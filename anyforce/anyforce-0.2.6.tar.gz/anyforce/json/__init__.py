from datetime import datetime
from typing import Any, Union

import orjson
from fastapi.encoders import jsonable_encoder


def fast_dumps(o: Any) -> str:
    return orjson.dumps(o).decode("utf-8")


def dumps(o: Any) -> str:
    return orjson.dumps(o, default=jsonable_encoder).decode("utf-8")


def loads(raw: Union[bytes, bytearray, str]):
    o = orjson.loads(raw)
    for k, v in o.items():
        if isinstance(v, str) and v.find("T") == 10:
            try:
                o[k] = datetime.fromisoformat(v)
            except ValueError:
                pass
    return o
