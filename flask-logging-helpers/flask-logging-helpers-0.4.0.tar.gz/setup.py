# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flask_logging', 'flask_logging.handlers']

package_data = \
{'': ['*']}

install_requires = \
['blinker>=1.4,<2.0', 'flask>=1.1.2,<2.0.0', 'pyyaml>=5.3.1,<6.0.0']

extras_require = \
{'docker': ['docker>=4.4.4,<5.0.0'], 'redis': ['redis>=3.5.3,<4.0.0']}

setup_kwargs = {
    'name': 'flask-logging-helpers',
    'version': '0.4.0',
    'description': 'Logging tools for flask',
    'long_description': None,
    'author': 'Alex Rudy',
    'author_email': 'opensource@alexrudy.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
