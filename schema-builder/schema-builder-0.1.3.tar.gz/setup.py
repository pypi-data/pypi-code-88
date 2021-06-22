# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schema_builder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'schema-builder',
    'version': '0.1.3',
    'description': 'Build JSON schemas from database tables.',
    'long_description': None,
    'author': 'Jordan Williams',
    'author_email': 'jordan.wallace.williams@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
