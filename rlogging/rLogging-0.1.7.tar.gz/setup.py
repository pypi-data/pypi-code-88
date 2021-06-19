# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rlogging',
 'rlogging.integration',
 'rlogging.integration.django',
 'rlogging.service']

package_data = \
{'': ['*']}

install_requires = \
['daemons==1.3.2', 'pyzmq==22.0.3', 'zmq==0.0.0']

setup_kwargs = {
    'name': 'rlogging',
    'version': '0.1.7',
    'description': 'Модуль гибкого логирования python приложений',
    'long_description': '# rlogging\n\nМодуль для логирования приложений python',
    'author': 'rocshers',
    'author_email': 'prog.rocshers@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
