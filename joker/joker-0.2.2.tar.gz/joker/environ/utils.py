#!/usr/bin/env python3
# coding: utf-8

import os


def load_modules_under_package(package, module_names=None):
    import re
    import importlib
    if isinstance(package, str):
        package = importlib.import_module(package)
    prefix = package.__name__
    match = re.compile(r'^[^_].*\.pyc?$').match

    # by default import all modules under package
    if module_names is None:
        d = os.path.split(package.__file__)[0]
        module_names = (x for x in os.listdir(d) if match(x))
        module_names = (x.split('.')[0] for x in module_names)
        module_names = list(module_names)

    loaded = list()
    for name in module_names:
        mp = '{}.{}'.format(prefix, name)
        loaded.append(importlib.import_module(mp))
    return loaded
