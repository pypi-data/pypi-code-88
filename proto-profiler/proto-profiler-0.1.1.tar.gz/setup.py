# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proto_profiler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'proto-profiler',
    'version': '0.1.1',
    'description': 'Profiler for stream of Protobuf messages',
    'long_description': None,
    'author': 'Ryan Brigden',
    'author_email': 'rpb@hey.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
