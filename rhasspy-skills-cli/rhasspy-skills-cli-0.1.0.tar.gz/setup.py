# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rhasspy_skills_cli']

package_data = \
{'': ['*']}

install_requires = \
['GitPython==3.1.18', 'httpx==0.18.2', 'pydantic==1.8.2', 'typer==0.3.2']

entry_points = \
{'console_scripts': ['rhskill = rhasspy_skills_cli.main:app']}

setup_kwargs = {
    'name': 'rhasspy-skills-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Rhasspy skills cli\nThis application can be use to install, create and delete skill managed by [rhasspy skills](https://github.com/razzo04/rhasspy-skills).\n\n',
    'author': 'razzo04',
    'author_email': 'razzorazzo1@gmail.com',
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
