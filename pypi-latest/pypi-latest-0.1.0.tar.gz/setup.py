# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypi_latest']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'click>=8.0.0,<9.0.0',
 'questionary>=1.9.0,<2.0.0',
 'rich>=10.4.0,<11.0.0']

entry_points = \
{'console_scripts': ['pypi-latest = pypi_latest.__main__:main']}

setup_kwargs = {
    'name': 'pypi-latest',
    'version': '0.1.0',
    'description': 'Verify that currently installed version is the latest one released on PyPI and update it if not.',
    'long_description': 'pypi-latest\n===========================\n\n|PyPI| |Python Version| |License| |Read the Docs| |Build| |Tests| |Codecov| |pre-commit| |Black|\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/pypi-latest.svg\n   :target: https://pypi.org/project/pypi-latest/\n   :alt: PyPI\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/pypi-latest\n   :target: https://pypi.org/project/pypi-latest\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/github/license/cookiejar/pypi-latest\n   :target: https://opensource.org/licenses/Apache2.0\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/pypi-latest/latest.svg?label=Read%20the%20Docs\n   :target: https://pypi-latest.readthedocs.io/\n   :alt: Read the documentation at https://pypi-latest.readthedocs.io/\n.. |Build| image:: https://github.com/cookiejar/pypi-latest/workflows/Build%20pypi-latest%20Package/badge.svg\n   :target: https://github.com/cookiejar/pypi-latest/actions?workflow=Package\n   :alt: Build Package Status\n.. |Tests| image:: https://github.com/cookiejar/pypi-latest/workflows/Run%20pypi-latest%20Tests/badge.svg\n   :target: https://github.com/cookiejar/pypi-latest/actions?workflow=Tests\n   :alt: Run Tests Status\n.. |Codecov| image:: https://codecov.io/gh/cookiejar/pypi-latest/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/cookiejar/pypi-latest\n   :alt: Codecov\n.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n   :target: https://github.com/pre-commit/pre-commit\n   :alt: pre-commit\n.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Black\n\n\nFeatures\n--------\n\n* Check whether the locally installed version of a Python package is the most recent version on PyPI\n* Prompt to update to the latest version if required\n\n\nInstallation\n------------\n\nYou can install *pypi-latest* via pip_ from PyPI_:\n\n.. code:: console\n\n   $ pip install pypi-latest\n\n\nUsage\n-----\n\nPlease see the `Usage Reference <Usage_>`_ for details.\n\n\nCredits\n-------\n\nThis package was created with cookietemple_ using Cookiecutter_ based on Hypermodern_Python_Cookiecutter_.\n\n.. _cookietemple: https://cookietemple.com\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _PyPI: https://pypi.org/\n.. _Hypermodern_Python_Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python\n.. _pip: https://pip.pypa.io/\n.. _Usage: https://pypi-latest.readthedocs.io/en/latest/usage.html\n',
    'author': 'Lukas Heumos',
    'author_email': 'lukas.heumos@posteo.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cookiejar/pypi-latest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<3.10',
}


setup(**setup_kwargs)
