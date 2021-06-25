# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cloudconnectlib',
 'cloudconnectlib.common',
 'cloudconnectlib.configuration',
 'cloudconnectlib.core',
 'cloudconnectlib.core.cacerts',
 'cloudconnectlib.splunktacollectorlib',
 'cloudconnectlib.splunktacollectorlib.common',
 'cloudconnectlib.splunktacollectorlib.data_collection']

package_data = \
{'': ['*']}

install_requires = \
['decorator>=4,<5',
 'future',
 'httplib2>=0.19.1,<0.20.0',
 'jinja2>=2.11.3,<3.0.0',
 'jsl>=0.2.4,<0.3.0',
 'jsonpath-ng>=1.5.2,<2.0.0',
 'jsonpath-rw>=1.4.0,<2.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'munch>=2.3.2,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'six',
 'solnlib>=4.1.0,<5.0.0',
 'sortedcontainers>=2.3.0,<3.0.0',
 'splunk-sdk>=1.6,<2.0',
 'splunktalib>=2,<3',
 'splunktaucclib>=5,<6']

setup_kwargs = {
    'name': 'cloudconnectlib',
    'version': '3.0.1b1',
    'description': 'APP Cloud Connect',
    'long_description': None,
    'author': 'Addon Factory template',
    'author_email': 'addonfactory@splunk.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
