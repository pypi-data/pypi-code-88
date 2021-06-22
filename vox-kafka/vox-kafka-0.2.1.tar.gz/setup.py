# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vox_kafka', 'vox_kafka.healthcheck']

package_data = \
{'': ['*']}

install_requires = \
['kafka-python']

setup_kwargs = {
    'name': 'vox-kafka',
    'version': '0.2.1',
    'description': 'Sinple kafka abstraction',
    'long_description': None,
    'author': 'Jhonatan Teixeira',
    'author_email': 'jhonatan.teixeira@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
