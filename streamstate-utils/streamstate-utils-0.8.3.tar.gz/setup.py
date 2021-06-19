# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['streamstate_utils']

package_data = \
{'': ['*']}

install_requires = \
['firebase-admin>=5.0.0,<6.0.0',
 'google-auth>=1.29.0,<2.0.0',
 'google-cloud-storage>=1.37.1,<2.0.0',
 'pydantic>=1.8.2,<2.0.0']

entry_points = \
{'console_scripts': ['run-test = streamstate_utils.run_test:main']}

setup_kwargs = {
    'name': 'streamstate-utils',
    'version': '0.8.3',
    'description': 'Utilities for firebase and spark streaming specifically for streamstate',
    'long_description': None,
    'author': 'Daniel Stahl',
    'author_email': 'danstahl1138@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/StreamState/streamstate-utils',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
