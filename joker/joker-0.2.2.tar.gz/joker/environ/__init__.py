#!/usr/bin/env python3
# coding: utf-8
__version__ = '0.2.2'

import os

import volkanic
from volkanic.compat import cached_property


class GlobalInterface(volkanic.GlobalInterface):
    package_name = 'joker.environ'

    @cached_property
    def _joker_dir(self):
        path = os.environ.get('JOKER_HOME', self.under_home_dir('.joker'))
        os.makedirs(path, int('700', 8), exist_ok=True)
        return path

    def under_joker_dir(self, *paths):
        return os.path.join(self._joker_dir, *paths)


__gi = GlobalInterface()


def under_joker_dir(*paths):
    return __gi.under_joker_dir(*paths)


# deprecated
def make_joker_dir(*paths):
    return under_joker_dir(*paths)


def _get_joker_packages():
    import pkg_resources
    packages = []
    for pkg in pkg_resources.working_set:
        pn = pkg.project_name
        if pn.startswith('joker-') or pn == 'joker':
            packages.append(pkg)


def _get_joker_packages_with_pkgutil():
    import pkgutil
    import joker
    # https://stackoverflow.com/a/57873844/2925169
    return list(pkgutil.iter_modules(
        joker.__path__,
        joker.__name__ + "."
    ))


def get_joker_packages(use_pkgutil=False):
    if use_pkgutil:
        return _get_joker_packages_with_pkgutil()
    else:
        return _get_joker_packages()
