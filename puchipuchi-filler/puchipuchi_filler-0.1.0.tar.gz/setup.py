# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['puchipuchi_filler',
 'puchipuchi_filler.puchipuchi_filler',
 'puchipuchi_filler.tests']

package_data = \
{'': ['*'], 'puchipuchi_filler': ['dist/*']}

setup_kwargs = {
    'name': 'puchipuchi-filler',
    'version': '0.1.0',
    'description': 'nothing to describe',
    'long_description': None,
    'author': 'snara tkomatsu tkano',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
