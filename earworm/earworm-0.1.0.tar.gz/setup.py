# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['earworm']

package_data = \
{'': ['*'], 'earworm': ['static/*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'Pillow>=8.2.0,<9.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'tinytag>=1.5.0,<2.0.0',
 'webassets>=2.0,<3.0']

entry_points = \
{'console_scripts': ['earworm = earworm.generate:main']}

setup_kwargs = {
    'name': 'earworm',
    'version': '0.1.0',
    'description': 'Create a simple web page to listen to audio files in a directory',
    'long_description': None,
    'author': 'Puneeth Chaganti',
    'author_email': 'punchagan@muse-amuse.in',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
