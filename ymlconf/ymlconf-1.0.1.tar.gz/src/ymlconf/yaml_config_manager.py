#!/usr/bin/env python3
import abc
from pathlib import Path

from .attribute import Attribute
from .common import dump_yaml, load_yaml

__all__ = [
    "YamlConfigError",
    "YamlConfigManager",
]


class YamlConfigError(Exception):
    pass


class YamlFileContentError(YamlConfigError):
    pass


class NoneValue(YamlConfigError):
    pass


class YamlConfigManager(metaclass=abc.ABCMeta):
    _KEY = ""

    def __new__(cls, *args, **kwargs):
        instance = super(YamlConfigManager, cls).__new__(cls)

        # init descriptors, make them exist in instance.__dict__
        for key, value in cls.__dict__.items():
            if isinstance(value, Attribute):
                getattr(instance, key)

        return instance

    def __init_subclass__(cls, **kwargs):
        # check type of key
        if not isinstance(cls._KEY, str):
            raise RuntimeError(f"expect str for KEY, but {type(cls._KEY)} was given!")

        # use class name as default key
        if not cls._KEY:
            cls._KEY = cls.__name__

    def __init__(self, path):
        self.path = Path(path)

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path):
        path = Path(path)

        if not path.is_file():
            raise FileNotFoundError(f"file: {path} dose not exist!")

        self._path = path.resolve()
        self._load()

    def _load_file_content(self) -> dict:
        file_content = load_yaml(self.path)

        if not isinstance(file_content, dict):
            raise YamlFileContentError(
                f"expect dict file content, while input is: {type(file_content)}"
            )

        return file_content

    def _get_object_content(self, file_content: dict) -> dict:
        object_content = file_content

        # extract object content from file
        names = self._KEY.split(".")
        for name in names:
            if name not in object_content:
                raise YamlFileContentError(
                    f"dict file dose not have expected key: {self._KEY}"
                )
            object_content = object_content[name]

        return object_content

    def _load(self):
        file_content = self._load_file_content()
        object_content = self._get_object_content(file_content)

        keys1 = set(object_content.keys())
        keys2 = set(self.__dict__.keys())
        diff_keys = keys1 - keys2

        if diff_keys:
            raise YamlFileContentError(f"incompatible keys: {diff_keys}")

        self.__dict__.update(**object_content)

    @classmethod
    def _check_object_content(cls, object_content: dict, allow_none_value):
        for key, value in object_content.items():
            if value is None and not allow_none_value:
                raise NoneValue(f"value of: {key} is None!")

    def _merge_self(self, object_content: dict):
        for key in object_content.keys():
            object_content[key] = getattr(self, key)

    def _dump(self, safety, allow_none_value):
        file_content = self._load_file_content()
        object_content = self._get_object_content(file_content)

        self._merge_self(object_content)

        self._check_object_content(object_content, allow_none_value)

        if not safety:
            dump_yaml(file_content, self.path)
            return

        temp_filename = self.path.with_suffix(".temp" + self.path.suffix)
        dump_yaml(file_content, temp_filename)
        temp_filename.rename(self.path)

    def reload(self):
        self._load()

    def flush(self, safety=True, allow_none_value=False):
        self._dump(safety, allow_none_value)
