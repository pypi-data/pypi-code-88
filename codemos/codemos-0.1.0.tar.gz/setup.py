# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codemos']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0', 'fastapi>=0.65.2,<0.66.0', 'requests>=2.25.1,<3.0.0']

setup_kwargs = {
    'name': 'codemos',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Nathanaël',
    'author_email': 'roipoussiere@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
