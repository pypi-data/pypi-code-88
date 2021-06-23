# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neogiinstruments']

package_data = \
{'': ['*']}

install_requires = \
['PyVISA-py>=0.5.2,<0.6.0',
 'matplotlib>=3.4.2,<4.0.0',
 'nidaqmx>=0.5.7,<0.6.0',
 'plotly>=5.0.0,<6.0.0',
 'pyserial>=3.5,<4.0']

setup_kwargs = {
    'name': 'neogiinstruments',
    'version': '0.1.1',
    'description': 'Communication and helper functions for lab equipment',
    'long_description': '# Instruments\nCommunication and helper functions for lab equipment\n',
    'author': 'UNT Neogi Lab',
    'author_email': 'BrianSquires@my.unt.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
