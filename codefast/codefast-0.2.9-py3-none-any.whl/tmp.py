#!/usr/bin/env python

from .utils import FileIO as io
import os


def abspath(_path: str):
    _path.lstrip('/tmp')
    return os.path.join('/tmp', _path)
