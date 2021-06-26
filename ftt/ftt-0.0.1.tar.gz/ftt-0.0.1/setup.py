# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ftt']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ftt',
    'version': '0.0.1',
    'description': 'Financial Trading Tools Project',
    'long_description': None,
    'author': 'Artem Melnykov',
    'author_email': 'melnykov.artem.v@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
