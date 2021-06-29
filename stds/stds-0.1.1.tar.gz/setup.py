# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stds']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stds',
    'version': '0.1.1',
    'description': 'A module for interacting with stdin, stdout and stderr.',
    'long_description': '# stds\n\n## Motivation\n\nThis is a small package that provides 3 high-level APIs to interact elegantly with stdin, stdout and stderr:\n\n    - stdin\n    - stderr\n    - stdout\n\n## Usage\n\nYou can use it as such:\n\n``` \nif __name__ == "__main__":\n    stdin | print\n    "This prints out stuff on stdout" | stdout\n    "This prints out stuff on stderr" | stderr\n```\n',
    'author': '4thel00z',
    'author_email': '4thel00z@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/4thel00z/std',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3,<4',
}


setup(**setup_kwargs)
