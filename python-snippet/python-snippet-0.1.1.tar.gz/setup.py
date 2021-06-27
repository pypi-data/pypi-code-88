# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_snippet']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'questionary>=1.9.0,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'rich>=10.4.0,<11.0.0',
 'textdistance>=4.2.1,<5.0.0',
 'typer-cli>=0.0.11,<0.0.12',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['python_snippet = python_snippet.main:app']}

setup_kwargs = {
    'name': 'python-snippet',
    'version': '0.1.1',
    'description': 'Python and Data Science Snippets on the command line',
    'long_description': '# Python Snippet Tool\n\nA tool to get Python and data science snippets at [Data Science Simplified](https://mathdatasimplified.com/) on the command line. \n\n## Installation\n```bash\npip install --user python-snippet\n```',
    'author': 'khuyentran1401',
    'author_email': 'khuyentran1476@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/khuyentran1401/python_snippet.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<3.10',
}


setup(**setup_kwargs)
