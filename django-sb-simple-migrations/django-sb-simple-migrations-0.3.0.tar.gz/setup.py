# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_sb_simple_migrations',
 'django_sb_simple_migrations.management',
 'django_sb_simple_migrations.management.commands',
 'django_sb_simple_migrations.migrations']

package_data = \
{'': ['*']}

install_requires = \
['Django<4.0.0']

setup_kwargs = {
    'name': 'django-sb-simple-migrations',
    'version': '0.3.0',
    'description': 'Django migrations without unnecesary change alert triggers.',
    'long_description': '![Community project](https://raw.githubusercontent.com/softbutterfly/django-sb-simple-migrations/master/resources/softbutterfly-open-source-community-project.png)\n\n![PyPI - Supported versions](https://img.shields.io/pypi/pyversions/django-sb-simple-migrations)\n![PyPI - Package version](https://img.shields.io/pypi/v/django-sb-simple-migrations)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/django-sb-simple-migrations)\n![PyPI - MIT License](https://img.shields.io/pypi/l/django-sb-simple-migrations)\n\n[![Build Status](https://www.travis-ci.org/softbutterfly/django-sb-simple-migrations.svg?branch=develop)](https://www.travis-ci.org/softbutterfly/django-sb-simple-migrations)\n[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9ed3b8725e094a648b38b96a3acdc1eb)](https://www.codacy.com/gh/softbutterfly/django-sb-simple-migrations/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=softbutterfly/django-sb-simple-migrations&amp;utm_campaign=Badge_Grade)\n[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/9ed3b8725e094a648b38b96a3acdc1eb)](https://www.codacy.com/gh/softbutterfly/django-sb-simple-migrations/dashboard?utm_source=github.com&utm_medium=referral&utm_content=softbutterfly/django-sb-simple-migrations&utm_campaign=Badge_Coverage)\n[![codecov](https://codecov.io/gh/softbutterfly/django-sb-simple-migrations/branch/master/graph/badge.svg?token=pbqXUUOu1F)](https://codecov.io/gh/softbutterfly/django-sb-simple-migrations)\n[![Requirements Status](https://requires.io/github/softbutterfly/django-sb-simple-migrations/requirements.svg?branch=master)](https://requires.io/github/softbutterfly/django-sb-simple-migrations/requirements/?branch=master)\n\n# Django Simple Migrations\n\nDjango migrations without unnecesary change alert triggers.\n\nThis project was originally taken from [Pretix source code](https://github.com/pretix/pretix/tree/master/src/pretix/base/management/commands) and battle testet across many projects on [SoftButterfly](https://softbutterfly.io).\n\nThis package overrides the commands `makemigrations` and `migrate`, mainly to make that `makemigrations` doesn\'t create migrations on non-significant database model fields and avoid `migrate` warnings. As is stated in the source code\n\n* `makemigrations`\n\n  > Django, for theoretically very valid reasons, creates migrations for *every single thing* we change on a model. Even the `help_text`! This makes sense, as we don\'t know if any database backend unknown to us might actually use this information for its database schema.\n  >\n  > However, many projects only supports PostgreSQL, MySQL, MariaDB and SQLite and we can be pretty certain that some changes to models will never require a change to the database. In this case, not creating a migration for certain changes will save us some performance while applying them *and* allow for a cleaner git history. Win-win!\n  >\n  > Only caveat is that we need to do some dirty monkeypatching to achieve it...\n\n* `migrate`\n\n  > Django tries to be helpful by suggesting to run "makemigrations" in red font on every "migrate" run when there are things we have no migrations for. Usually, this is intended, and running "makemigrations" can really screw up the environment of a user, so we want to prevent novice users from doing that by going really dirty and filtering it from the output.\n\n## Requirements\n\n- Python 3.6, 3.7, 3.8, 3.9\n\n## Install\n\n```bash\npip install django-sb-simple-migrations\n```\n\n## Usage\n\nJust add `django_sb_simple_migrations` to your `INSTALLED_APPS` settings\n\n```\nINSTALLED_APPS = [\n  # ...\n  "django_sb_simple_migrations",\n  # ...\n]\n```\n\n## Docs\n\n- [Ejemplos](https://github.com/softbutterfly/django-sb-simple-migrations/wiki)\n- [Wiki](https://github.com/softbutterfly/django-sb-simple-migrations/wiki)\n\n## Changelog\n\nAll changes to versions of this library are listed in the [change history](CHANGELOG.md).\n\n## Development\n\nCheck out our [contribution guide](CONTRIBUTING.md).\n\n## Contributors\n\nSee the list of contributors [here](https://github.com/softbutterfly/django-sb-simple-migrations/graphs/contributors).\n',
    'author': 'SoftButterfly Development Team',
    'author_email': 'dev@softbutterfly.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/softbutterfly/django-sb-simple-migrations',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
