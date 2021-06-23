# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['postcode_validator_uk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'postcode-validator-uk',
    'version': '1.0.0',
    'description': 'A simple UK postcode validator.',
    'long_description': None,
    'author': 'Guilherme Munarolo',
    'author_email': 'guimunarolo@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
