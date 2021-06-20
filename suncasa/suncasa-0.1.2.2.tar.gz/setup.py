#!/usr/bin/env python
from setuptools import setup
import os
from itertools import chain

from extension_helpers import get_extensions
from setuptools.config import read_configuration

################################################################################
# Programmatically generate some extras combos.
################################################################################
extras = read_configuration("setup.cfg")['options']['extras_require']

# Dev is everything
extras['dev'] = list(chain(*extras.values()))

# All is everything but tests and docs
exclude_keys = ("tests", "docs", "dev")
ex_extras = dict(filter(lambda i: i[0] not in exclude_keys, extras.items()))
# Concatenate all the values together for 'all'
extras['all'] = list(set(list(chain.from_iterable(ex_extras.values()))))

setup(
    extras_require=extras,
    # use_scm_version={'write_to': os.path.join('suncasa', '_version.py')},
    version='0.1.2.2',
    ext_modules=get_extensions(),
)
