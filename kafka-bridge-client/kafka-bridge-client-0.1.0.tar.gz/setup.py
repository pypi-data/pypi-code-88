# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kafka_bridge_client']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'kafka-bridge-client',
    'version': '0.1.0',
    'description': 'Python client for Strimzi Kafka Bridge',
    'long_description': None,
    'author': 'Bogdan Zaseka',
    'author_email': 'zaseka.bogdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
