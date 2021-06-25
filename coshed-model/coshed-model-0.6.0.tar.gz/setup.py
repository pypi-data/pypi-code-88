# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coshed_model']

package_data = \
{'': ['*']}

install_requires = \
['SQLAlchemy>=1.4.2,<2.0.0', 'djali>=0.2.0,<0.3.0', 'pendulum>=2.1.2,<3.0.0']

setup_kwargs = {
    'name': 'coshed-model',
    'version': '0.6.0',
    'description': '',
    'long_description': None,
    'author': 'doubleO8',
    'author_email': 'wb008@hdm-stuttgart.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
