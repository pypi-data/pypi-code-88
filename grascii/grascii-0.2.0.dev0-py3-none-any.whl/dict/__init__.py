
import io
from pathlib import Path
from typing import TextIO

from pkg_resources import resource_stream, resource_exists

from grascii.install import DICTIONARY_PATH

def get_dict_file(dictionary: str, name: str) -> TextIO:
    if dictionary[0] == ":":
        if not resource_exists("grascii.dict", dictionary[1:]):
            pass
        module = "grascii.dict." + dictionary[1:]
        return io.TextIOWrapper(resource_stream(module, name),
                encoding="utf-8")

    return DICTIONARY_PATH.joinpath(dictionary, name).open()


