#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" This package expose method to interact with astralbot. """
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

import os


def get_ressource(filename):
    """
        Return the path to an installed ressource file.
    """
    packagedir = __path__[0]
    dirname = os.path.join(os.path.dirname(packagedir), 'ressources')
    fullname = os.path.join(dirname, filename)
    return fullname


def get_version_from_ressource():
    """ Read the file and return the value """
    version_path = get_ressource('VERSION')
    with open(version_path) as version_file:
        version = version_file.read().strip()
    return version
