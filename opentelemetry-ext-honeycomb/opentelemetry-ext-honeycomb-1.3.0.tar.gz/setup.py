# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['opentelemetry', 'opentelemetry.ext', 'opentelemetry.ext.honeycomb']

package_data = \
{'': ['*']}

install_requires = \
['libhoney>=1.10.0', 'opentelemetry-api==1.3.0', 'opentelemetry-sdk==1.3.0']

setup_kwargs = {
    'name': 'opentelemetry-ext-honeycomb',
    'version': '1.3.0',
    'description': 'OpenTelemetry plugins for Honeycomb',
    'long_description': None,
    'author': 'Honeycomb Authors',
    'author_email': 'solutions@honeycomb.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
