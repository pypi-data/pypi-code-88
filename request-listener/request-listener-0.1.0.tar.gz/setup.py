# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['request_listener']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.65.2,<0.66.0',
 'install>=1.3.4,<2.0.0',
 'pip>=21.1.2,<22.0.0',
 'pyngrok>=5.0.5,<6.0.0',
 'uvicorn[standard]>=0.14.0,<0.15.0']

setup_kwargs = {
    'name': 'request-listener',
    'version': '0.1.0',
    'description': 'A simple way to explore incoming webhooks.',
    'long_description': None,
    'author': 'luttik',
    'author_email': 'dtluttik@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Luttik/request-listener',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
