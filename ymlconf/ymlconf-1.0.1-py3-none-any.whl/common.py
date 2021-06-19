#!/usr/bin/env python3

from pathlib import Path

import more_itertools
from ruamel.yaml import YAML

__all__ = [
    "load_yaml",
    "dump_yaml",
    "flatten_iter",
    "flatten_list",
]


class FileSuffixError(Exception):
    pass


def _check_yaml_file_suffix(path: Path):
    valid_suffixes = {".yaml", ".yml"}

    if path.suffix not in valid_suffixes:
        raise FileSuffixError(
            f"invalid file suffix: {path.suffix}, "
            f"it should be one of: {valid_suffixes}"
        )


def load_yaml(path):
    path = Path(path)

    _check_yaml_file_suffix(path)

    yaml = YAML(typ="safe")

    return yaml.load(path)


def dump_yaml(data, path):
    path = Path(path)

    _check_yaml_file_suffix(path)

    yaml = YAML()
    yaml.default_flow_style = False
    yaml.dump(data, path)


def flatten_iter(iterable):
    return more_itertools.collapse(iterable)


def flatten_list(iterable):
    return list(flatten_iter(iterable))
