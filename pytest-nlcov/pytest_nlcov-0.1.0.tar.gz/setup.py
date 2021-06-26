# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_nlcov']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.17,<4.0.0',
 'coverage>=5.5,<6.0',
 'pytest-cov>=2.10.1',
 'typer>=0.3.2,<0.4.0',
 'unidiff>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['nlcov = pytest_nlcov:cli'],
 'pytest11': ['nlcov = pytest_nlcov']}

setup_kwargs = {
    'name': 'pytest-nlcov',
    'version': '0.1.0',
    'description': '',
    'long_description': '# pytest_nlcov\n\nWith `pytest_nlcov` you can check the test coverage of new lines only. It will\ncheck git for added and modified lines and will compute the coverage\njust for those lines\n\n## Installation\n\n```sh\npip install pytest_nlcov\n```\n\nNote: `pytest_cov` is required and will be automatically installed when it \nis not installed yet.\n\n## Usage with pytest\n\nWhen `pytest_nlcov` is installed, it will be discovered by pytest and executed as last step to\nshow you the test coverage of new lines.\n\n```sh\npytest\n```\n\nTwo option can be given:\n\n- revision\n- fail threshold\n\n### Revision\n\nDefault, the new lines are based on the git diff with master. You can specify other revisions.\n\n```sh\npytest --nlcov-revision main\n```\n\n### Fail Threshold\n\nOptionally you can add a threshold to fail the tests when the coverage is below the threshold.\n\n```sh\npytest --nlcov-fail-under 0.6\n```\n\n## Usage without pytest\n\n`pytest_nlcov` can be run without pytest. Therefor you have to run `coverage` first, because `pytest_nlcov`\nneeds its coverage data.\n\n```sh\ncoverage\nnlcov\n```\n\nOptionally a revision can be given\n\n```sh\nnlcov main\n```\n',
    'author': 'Marc Rijken',
    'author_email': 'marc@rijken.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mrijken/pytest_nlcov',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)
