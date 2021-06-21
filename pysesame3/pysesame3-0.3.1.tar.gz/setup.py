# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysesame3', 'tests']

package_data = \
{'': ['*'], 'tests': ['fixtures/*']}

install_requires = \
['pycryptodome>=3.10.1,<4.0.0', 'requests>=2.25.1,<3.0.0']

extras_require = \
{'cognito': ['AWSIoTPythonSDK>=1.4.9,<2.0.0',
             'boto3>=1.17.94,<2.0.0',
             'certifi',
             'requests-aws4auth>=1.1.1,<2.0.0'],
 'doc': ['livereload>=2.6.3,<3.0.0',
         'mkdocs>=1.1.2,<2.0.0',
         'mkdocstrings>=0.15.0,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0',
         'mkdocs-include-markdown-plugin>=3.1.3,<4.0.0',
         'mkdocs-material>=7.1.8,<8.0.0']}

setup_kwargs = {
    'name': 'pysesame3',
    'version': '0.3.1',
    'description': 'Unofficial library to communicate with Sesame smart locks.',
    'long_description': '# pysesame3\n\n_Unofficial Python Library to communicate with Sesame smart locks made by CANDY HOUSE, Inc._\n\n[![PyPI](https://img.shields.io/pypi/v/pysesame3)](https://pypi.python.org/pypi/pysesame3)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pysesame3)\n![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/mochipon/pysesame3/dev%20workflow/main)\n[![Documentation Status](https://readthedocs.org/projects/pysesame3/badge/?version=latest)](https://pysesame3.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/mochipon/pysesame3/branch/main/graph/badge.svg?token=2Y7OPZTILT)](https://codecov.io/gh/mochipon/pysesame3)\n![PyPI - License](https://img.shields.io/pypi/l/pysesame3)\n\n* Free software: MIT license\n* Documentation: [https://pysesame3.readthedocs.io](https://pysesame3.readthedocs.io)\n\n## Features\n\nPlease note that `pysesame3` can only control [SESAME 3](https://jp.candyhouse.co/products/sesame3) at this moment.\n\n* Retrive a list of SESAME locks that the user is authorized to use.\n* Retrive a status of a SESAME lock (locked, handle position, etc.).\n* Retrive recent events (locked, unlocked, etc.) associated with a lock.\n* Needless to say, locking and unlocking!\n\n## Usage\n\nPlease take a look at [the documentation](https://pysesame3.readthedocs.io/en/latest/usage/).\n\n## Credits & Thanks\n\n* A huge thank you to all who assisted with [CANDY HOUSE](https://jp.candyhouse.co/).\n* This project was inspired and based on [tchellomello/python-ring-doorbell](https://github.com/tchellomello/python-ring-doorbell) and [snjoetw/py-august](https://github.com/snjoetw/py-august).\n',
    'author': 'Masaki Tagawa',
    'author_email': 'masaki@tagawa.email',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mochipon/pysesame3',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
