# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['DrukBam']

package_data = \
{'': ['*']}

install_requires = \
['cython>=0.29,<0.30',
 'matplotlib>=3.4.2,<4.0.0',
 'pandas>=1.2.4,<2.0.0',
 'pysam>=0.16.0,<0.17.0',
 'tqdm>=4.61.1,<5.0.0']

entry_points = \
{'console_scripts': ['DrukBam = DrukBam.__main__:main']}

setup_kwargs = {
    'name': 'drukbam',
    'version': '0.1.2.1',
    'description': 'Comandline plotting of sort,indexed bam files',
    'long_description': None,
    'author': 'Stephan Holger Drukewitz',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1,<4.0.0',
}


setup(**setup_kwargs)
