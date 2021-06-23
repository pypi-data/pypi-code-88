# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['schematic',
 'schematic.manifest',
 'schematic.models',
 'schematic.schemas',
 'schematic.store',
 'schematic.utils']

package_data = \
{'': ['*'],
 'schematic': ['etc/*', 'etc/data_models/*', 'etc/validation_schemas/*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'click-log>=0.3.2,<0.4.0',
 'click>=7.1.2,<8.0.0',
 'google-api-python-client>=1.12.8,<2.0.0',
 'google-auth-httplib2>=0.0.4,<0.0.5',
 'google-auth-oauthlib>=0.4.2,<0.5.0',
 'graphviz>=0.16,<0.17',
 'inflection>=0.5.1,<0.6.0',
 'jsonschema>=3.2.0,<4.0.0',
 'networkx>=2.5,<3.0',
 'oauth2client<4.0.0',
 'pandas>=1.2.1,<2.0.0',
 'pygsheets>=2.0.4,<3.0.0',
 'rdflib>=5.0.0,<6.0.0',
 'setuptools>=52.0.0,<53.0.0',
 'synapseclient>=2.3,<2.4',
 'toml>=0.10.2,<0.11.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.6.0,<2.0.0']}

entry_points = \
{'console_scripts': ['schematic = schematic.__main__:main']}

setup_kwargs = {
    'name': 'schematicpy',
    'version': '1.0.0',
    'description': 'Package for biomedical data model and metadata ingress management',
    'long_description': '# Schematic\n[![Build Status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2FSage-Bionetworks%2Fschematic%2Fbadge%3Fref%3Ddevelop&style=flat)](https://actions-badge.atrox.dev/Sage-Bionetworks/schematic/goto?ref=develop) [![Documentation Status](https://readthedocs.org/projects/sage-schematic/badge/?version=develop)](https://sage-schematic.readthedocs.io/en/develop/?badge=develop) [![PyPI version](https://badge.fury.io/py/schematicpy.svg)](https://badge.fury.io/py/schematicpy)\n\n## Introduction\n\nSCHEMATIC is an acronym for _Schema Engine for Manifest Ingress and Curation_. The Python based infrastructure provides a _novel_ schema-based, data ingress ecosystem, that is meant to streamline the process of dataset annotation, metadata validation and submission to an asset store for various data contributors.\n\n## Installation Requirements and Pre-requisites\n\n* Python 3.7.1 or higher\n\nNote: You need to be a registered and certified user on [`synapse.org`](https://www.synapse.org/), and also have the right permissions to download the Google credentials files from Synapse.\n\n## Installing\n\nCreate and activate a virtual environment within which you can install the package:\n\n```\npython -m venv .venv\nsource .venv/bin/activate\n```\n\nInstall and update the package using [pip](https://pip.pypa.io/en/stable/quickstart/):\n\n```\npython -m pip install schematicpy\n```\n\n## Command Line Client Usage\n\n### Initialization\n\n```\nschematic init --config ~/path/to/config.yml    # initialize mode of authentication\n```\n\n### Manifest\n\n```\nschematic manifest --config ~/path/to/config.yml get    # generate manifest based on data type\n```\n\n```\nschematic manifest --config ~/path/to/config.yml validate   # validate manifest\n```\n\n### Model\n\n```\nschematic model --config ~/path/to/config.yml submit    # validate and submit manifest\n```\n\n## Contributing\n\nInterested in contributing? Awesome! We follow the typical [GitHub workflow](https://guides.github.com/introduction/flow/) of forking a repo, creating a branch, and opening pull requests. For more information on how you can add or propose a change, visit our [contributing guide](CONTRIBUTION.md). To start contributing to the package, you can refer to the [Getting Started](CONTRIBUTION.md#getting-started) section in our [contributing guide](CONTRIBUTION.md).\n\n## Contributors\n\nActive contributors and maintainers:\n\n- [Milen Nikolov](https://github.com/milen-sage)\n- [Sujay Patil](https://github.com/sujaypatil96)\n- [Bruno Grande](https://github.com/BrunoGrandePhD)\n- [Xengie Doan](https://github.com/xdoan)\n',
    'author': 'Milen Nikolov',
    'author_email': 'milen.nikolov@sagebase.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Sage-Bionetworks/schematic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
