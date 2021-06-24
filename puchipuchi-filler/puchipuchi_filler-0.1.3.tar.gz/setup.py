# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['puchipuchi_filler']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['puchipuchi_filler = puchipuchi_filler.main:main']}

setup_kwargs = {
    'name': 'puchipuchi-filler',
    'version': '0.1.3',
    'description': 'nothing',
    'long_description': '## puchipuchi_filler\n何もしません\n',
    'author': 'puchipuchi team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
