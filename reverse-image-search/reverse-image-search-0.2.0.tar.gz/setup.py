# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reverse_image_search']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.0.1,<2.0.0',
 'opencv-python>=4.5.2,<5.0.0',
 'scikit-image>=0.18.1,<0.19.0',
 'tabulate>=0.8.9,<0.9.0']

entry_points = \
{'console_scripts': ['reverse_image_search = reverse_image_search.cli:cli']}

setup_kwargs = {
    'name': 'reverse-image-search',
    'version': '0.2.0',
    'description': 'Reverse Image Search',
    'long_description': None,
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
