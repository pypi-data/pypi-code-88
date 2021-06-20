import datetime
from typing import Sequence


def append_timestamp(file_contents: Sequence[str]) -> Sequence[str]:
    return file_contents + [f"[{datetime.datetime.now().isoformat()}] "]

