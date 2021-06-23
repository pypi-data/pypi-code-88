import datetime
from typing import Mapping
from typing import Sequence


def get_timestamp(stamp_format: str = "%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.now().strftime(stamp_format)


def append_timestamp(
    file_contents: Sequence[str], extension_config: Mapping = {}
) -> Sequence[str]:
    stamp_format = (
        "%Y-%m-%d %H:%M:%S"
        if not "format" in extension_config
        else extension_config["format"]
    )
    prefix = "\n[" if not 'prefix' in extension_config else extension_config["prefix"]
    suffix = "] " if not 'suffix' in extension_config else extension_config["suffix"]
    now = get_timestamp(stamp_format)
    return file_contents + [f"{prefix}{now}{suffix}"]
