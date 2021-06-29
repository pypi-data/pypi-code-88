# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['slurmops']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.1,<6.0',
 'boto3>=1.17.99,<2.0.0',
 'docker>=5.0.0,<6.0.0',
 'python_json_logger>=0.1,<0.2',
 'requests_mock>=1.9,<2.0',
 'sshpubkeys>=3.3.1,<4.0.0']

setup_kwargs = {
    'name': 'slurmops',
    'version': '0.0.1',
    'description': 'NVIDIA/DeepOps on AWS EC2',
    'long_description': '# SlurmOps\n\n[![Python](docs/img/badges/language.svg)](https://devdocs.io/python/)\n\nNVIDIA/DeepOps on AWS EC2.\n\n## Usage\n\nWIP\n\n## Contributing\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md)\n',
    'author': 'Leo Gallucci',
    'author_email': 'elgalu3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/elgalu/slurmops',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
