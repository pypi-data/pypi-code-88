# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['alife']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.18,<4.0.0', 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['alife = alife.cli:run']}

setup_kwargs = {
    'name': 'alife',
    'version': '0.1.0',
    'description': 'Git a Life',
    'long_description': None,
    'author': 'Bijay Gurung',
    'author_email': 'bijay.learning@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
