# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stimpy', 'stimpy.animate']

package_data = \
{'': ['*']}

install_requires = \
['PsychoPy>=2021.2.0,<2022.0.0', 'numpy>=1.21.0,<2.0.0']

setup_kwargs = {
    'name': 'stimpy',
    'version': '0.0.1',
    'description': 'A PsychoPy wrapper to create moving visual stimuli without loops.',
    'long_description': None,
    'author': 'Ka Chung Lam',
    'author_email': 'kclamar@connect.ust.hk',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
