# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['leapcli']

package_data = \
{'': ['*']}

install_requires = \
['docopt>=0.6.2,<0.7.0']

entry_points = \
{'console_scripts': ['leap = leapcli.cli:__main__']}

setup_kwargs = {
    'name': 'leapcli',
    'version': '0.1.1',
    'description': 'Tensorleap CLI',
    'long_description': None,
    'author': 'Assaf Lavie',
    'author_email': 'assaf.lavie@tensorleap.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tensorleap/cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
