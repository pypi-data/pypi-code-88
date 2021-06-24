# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['komolibs',
 'komolibs.core',
 'komolibs.core.utils',
 'komolibs.logger',
 'komolibs.messaging',
 'komolibs.pubsub']

package_data = \
{'': ['*']}

install_requires = \
['aiokafka>=0.7.1,<0.8.0',
 'aioredis>=1.3.1,<2.0.0',
 'avro>=1.10.2,<2.0.0',
 'certifi>=2021.5.30,<2022.0.0',
 'confluent-kafka>=1.7.0,<2.0.0',
 'kafka-python>=2.0.2,<3.0.0']

setup_kwargs = {
    'name': 'komolibs',
    'version': '0.1.11',
    'description': '',
    'long_description': None,
    'author': 'Khosi Morafo',
    'author_email': 'khosimorafo@yahoo.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
