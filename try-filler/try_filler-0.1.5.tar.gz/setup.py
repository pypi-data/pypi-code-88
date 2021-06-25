# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['try_filler']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['try_filler = try_filler.cli:main']}

setup_kwargs = {
    'name': 'try-filler',
    'version': '0.1.5',
    'description': '',
    'long_description': None,
    'author': 'Team TRY',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
