# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rcore', 'rcore.exception', 'rcore.sync', 'rcore.venv']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml==5.4.1', 'rlogging>=0.1.8,<0.2.0']

setup_kwargs = {
    'name': 'rcore',
    'version': '0.1.9',
    'description': 'Ядро для приложений python. Сборник утилит.',
    'long_description': '# rcore\n\nЯдро для приложений python. Сборник утилит.\n',
    'author': 'rocshers',
    'author_email': 'prog.rocshers@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
