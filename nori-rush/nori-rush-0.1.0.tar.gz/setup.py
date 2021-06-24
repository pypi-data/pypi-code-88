# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nori_rush']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['nori_rush = nori_rush.nori.py:main']}

setup_kwargs = {
    'name': 'nori-rush',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'ntoshihi',
    'author_email': 'ntoshihi@student.42tokyo.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
