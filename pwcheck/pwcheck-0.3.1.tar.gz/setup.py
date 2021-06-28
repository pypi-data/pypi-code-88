# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pwcheck']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pwcheck',
    'version': '0.3.1',
    'description': 'Python Password Checker',
    'long_description': '========\nOverview\n========\n\n.. start-badges\n\n.. list-table::\n    :stub-columns: 1\n\n    * - docs\n      - |docs|\n    * - tests\n      - | |travis| |appveyor| |requires|\n        | |codecov|\n    * - package\n      - | |version| |wheel| |supported-versions| |supported-implementations|\n        | |commits-since|\n.. |docs| image:: https://readthedocs.org/projects/pwcheck/badge/?style=flat\n    :target: https://pwcheck.readthedocs.io/\n    :alt: Documentation Status\n\n.. |travis| image:: https://api.travis-ci.com/Itotutona/pwcheck.svg?branch=master\n    :alt: Travis-CI Build Status\n    :target: https://travis-ci.com/github/Itotutona/pwcheck\n\n.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/Itotutona/pwcheck?branch=master&svg=true\n    :alt: AppVeyor Build Status\n    :target: https://ci.appveyor.com/project/Itotutona/pwcheck\n\n.. |requires| image:: https://requires.io/github/Itotutona/pwcheck/requirements.svg?branch=master\n    :alt: Requirements Status\n    :target: https://requires.io/github/Itotutona/pwcheck/requirements/?branch=master\n\n.. |codecov| image:: https://codecov.io/gh/Itotutona/pwcheck/branch/master/graphs/badge.svg?branch=master\n    :alt: Coverage Status\n    :target: https://codecov.io/github/Itotutona/pwcheck\n\n.. |version| image:: https://img.shields.io/pypi/v/pwcheck.svg\n    :alt: PyPI Package latest release\n    :target: https://pypi.org/project/pwcheck\n\n.. |wheel| image:: https://img.shields.io/pypi/wheel/pwcheck.svg\n    :alt: PyPI Wheel\n    :target: https://pypi.org/project/pwcheck\n\n.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pwcheck.svg\n    :alt: Supported versions\n    :target: https://pypi.org/project/pwcheck\n\n.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pwcheck.svg\n    :alt: Supported implementations\n    :target: https://pypi.org/project/pwcheck\n\n.. |commits-since| image:: https://img.shields.io/github/commits-since/Itotutona/pwcheck/v0.1.0.svg\n    :alt: Commits since latest release\n    :target: https://github.com/Itotutona/pwcheck/compare/v0.1.0...master\n\n\n\n.. end-badges\n\nPython Password Checker\n\n* Free software: GNU Lesser General Public License v3 (LGPLv3)\n\nInstallation\n============\n\n::\n\n    pip install pwcheck\n\nYou can also install the in-development version with::\n\n    pip install https://github.com/Itotutona/pwcheck/archive/master.zip\n\n\nDocumentation\n=============\n\n\nhttps://pwcheck.readthedocs.io/\n\n\nDevelopment\n===========\n\nTo run all the tests run::\n\n    tox\n\nNote, to combine the coverage data from all the tox environments run:\n\n.. list-table::\n    :widths: 10 90\n    :stub-columns: 1\n\n    - - Windows\n      - ::\n\n            set PYTEST_ADDOPTS=--cov-append\n            tox\n\n    - - Other\n      - ::\n\n            PYTEST_ADDOPTS=--cov-append tox\n',
    'author': 'Itotutona',
    'author_email': 'itotutona.github@evta.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Itotutona/pwcheck',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
