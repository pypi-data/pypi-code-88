# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cr_kyoushi', 'cr_kyoushi.dataset', 'cr_kyoushi.dataset.files']

package_data = \
{'': ['*'], 'cr_kyoushi.dataset': ['templates/*']}

install_requires = \
['Jinja2>=2.11.3,<3.0.0',
 'aiohttp>=3.7.4,<4.0.0',
 'certifi>=2020.12.5,<2021.0.0',
 'click>=7.1.2,<8.0.0',
 'elasticsearch-dsl>=7.3.0,<8.0.0',
 'elasticsearch>=7.12.0,<8.0.0',
 'livereload>=2.6.3,<3.0.0',
 'pydantic>=1.8.1,<2.0.0',
 'pyshark>=0.4.3,<0.5.0',
 'ruamel.yaml>=0.17.2,<0.18.0',
 'ujson>=4.0.2,<5.0.0']

entry_points = \
{'console_scripts': ['cr-kyoushi-dataset = kyoushi.dataset.cli:cli']}

setup_kwargs = {
    'name': 'kyoushi-dataset',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Cyber Range Kyoushi - Dataset\nIDS dataset processing and labeling package for AECID datasets.\n',
    'author': 'Maximilian Frank',
    'author_email': 'maximilian.frank@ait.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git-service.ait.ac.at/sct-cyberrange/tools/kyoushi/dataset',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
