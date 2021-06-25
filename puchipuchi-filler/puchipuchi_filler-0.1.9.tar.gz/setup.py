# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['puchipuchi_filler']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['puchipuchi_filler = puchipuchi_filler.main:main']}

setup_kwargs = {
    'name': 'puchipuchi-filler',
    'version': '0.1.9',
    'description': 'no description provided',
    'long_description': '# puchipuchi-filler\nwe do nothing\n何もしないです\n\n',
    'author': 'puchipuchi team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
