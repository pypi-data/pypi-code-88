# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['django_sorting_bootstrap', 'django_sorting_bootstrap.templatetags']

package_data = \
{'': ['*'],
 'django_sorting_bootstrap': ['locale/de/LC_MESSAGES/*',
                              'templates/sorting_bootstrap/*']}

install_requires = \
['django>=2.0']

setup_kwargs = {
    'name': 'django-sorting-bootstrap',
    'version': '2.7.0',
    'description': 'Sorting templates API using sorting, Django templatetags and Bootstrap classes.',
    'long_description': "Django Sorting Bootstrap\n========================\n\n|PyPI| |Python Version| |License|\n\n|Read the Docs| |Tests|\n\n|pre-commit| |Black|\n\n.. |PyPI| image:: https://img.shields.io/pypi/v/django-sorting-bootstrap.svg\n   :target: https://pypi.org/project/django-sorting-bootstrap/\n   :alt: PyPI\n.. |Python Version| image:: https://img.shields.io/pypi/pyversions/django-sorting-bootstrap\n   :target: https://pypi.org/project/django-sorting-bootstrap\n   :alt: Python Version\n.. |License| image:: https://img.shields.io/pypi/l/django-sorting-bootstrap\n   :target: https://opensource.org/licenses/MIT\n   :alt: License\n.. |Read the Docs| image:: https://img.shields.io/readthedocs/django-sorting-bootstrap/latest.svg?label=Read%20the%20Docs\n   :target: https://django-sorting-bootstrap.readthedocs.io/\n   :alt: Read the documentation at https://django-sorting-bootstrap.readthedocs.io/\n.. |Tests| image:: https://github.com/staticdev/django-sorting-bootstrap/workflows/Tests/badge.svg\n   :target: https://github.com/staticdev/django-sorting-bootstrap/actions?workflow=Tests\n   :alt: Tests\n.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white\n   :target: https://github.com/pre-commit/pre-commit\n   :alt: pre-commit\n.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg\n   :target: https://github.com/psf/black\n   :alt: Black\n\n\nFeatures\n--------\n\nDjango Sorting Bootstrap is a pluggable mini-API to easy add sorting for querysets, links and table headers in Django_ templates. There is also a new tag that creates headers for sorting tables using Bootstrap_'s layout.\n\n\nRequirements\n------------\n\n* Python 3.7+\n* Django 2.0+\n* Bootstrap 3+\n\n\nInstallation\n------------\n\nYou can install *Django Sorting Bootstrap* via pip_ from PyPI_:\n\n.. code:: console\n\n   $ pip install django-sorting-bootstrap\n\n\nDocumentation\n-------------\n\nComplete instructions on installation and usage are found in ``docs`` directory and online at\nhttps://django-sorting-bootstrap.readthedocs.io.\n\n\nContributing\n------------\n\nContributions are very welcome.\nTo learn more, see the `Contributor Guide`_.\n\n\nLicense\n-------\n\nDistributed under the terms of the MIT_ license,\n*Django Sorting Bootstrap* is free and open source software.\n\n\nCredits\n-------\n\nThis app is based on `Agiliq's django-sorting`_ 0.1. It has two improvements over it: the new tags and the Twitter Bootstrap compliance idea.\n\n\n.. _issue here: https://github.com/staticdev/staticdev/issues\n.. _Django: https://www.djangoproject.com/\n.. _Bootstrap: http://getbootstrap.com/\n.. _MIT: http://opensource.org/licenses/MIT\n.. _PyPI: https://pypi.org/\n.. _pip: https://pip.pypa.io/\n.. _Agiliq's django-sorting: http://github.com/agiliq/django-sorting\n.. github-only\n.. _Contributor Guide: CONTRIBUTING.rst\n",
    'author': "Thiago D'Ávila",
    'author_email': 'staticdev-support@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/staticdev/django-sorting-bootstrap',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
