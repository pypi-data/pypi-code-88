# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['src', 'src.aws_in_docker']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.1,<6.0', 'python_json_logger>=0.1,<0.2']

setup_kwargs = {
    'name': 'slurm-in-aws',
    'version': '0.0.1',
    'description': 'AWS plugin for Slurm',
    'long_description': '# slurm_in_aws\n\n[![](docs/img/badges/language.svg)](https://devdocs.io/python/)\n\nMock EC2 with moto + launch instances in Docker.\n\n## Usage\n\n```sh\n# TODO\n```\n\n## Contributing\n\n### Contributing Setup\n\n1. Clone the project locally\n1. Install the corresponding [.python-version](./.python-version) using something like [pyenv](https://github.com/pyenv/pyenv)\n1. Create a virtual environment named `.venv` with `python -m venv .venv`\n1. Activate the virtual environment with `source .venv/bin/activate`\n1. Install [poetry](https://poetry.eustace.io/docs/#installation)\n1. Install [invoke](https://www.pyinvoke.org/installing.html) with `pip install invoke`\n1. Run `poetry install --no-root`\n1. Run `invoke setup`\n\n### Contributing Tests\n\nRun `poetry run invoke tests`\n\n### Contributing All Checks (including tests)\n\nRun `poetry run invoke hooks`\n\n### Build And Publish to PyPI\n\n```sh\npoetry build\npoetry publish\n```\n',
    'author': 'Leo Gallucci',
    'author_email': 'elgalu3@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
