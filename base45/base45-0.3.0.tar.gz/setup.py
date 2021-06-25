# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['base45']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['base45 = base45.cli:main']}

setup_kwargs = {
    'name': 'base45',
    'version': '0.3.0',
    'description': 'Base45 Encoder/Decoder',
    'long_description': '# Python Base45\n\nA Python module to encode/decode binary data using Base45 as described in [draft-faltstrom-base45-02 ](https://datatracker.ietf.org/doc/draft-faltstrom-base45/).\n',
    'author': 'Jakob Schlyter',
    'author_email': 'jakob@kirei.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kirei/python-base45',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
