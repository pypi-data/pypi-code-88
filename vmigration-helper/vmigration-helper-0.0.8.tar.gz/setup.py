# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vmigration_helper',
 'vmigration_helper.management',
 'vmigration_helper.management.commands',
 'vmigration_helper.migrations']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'vmigration-helper',
    'version': '0.0.8',
    'description': "Van's Django Migration Helper",
    'long_description': '# Van\'s Migration Helper\n\nDjango commands to help with running Django migrations.\n\n## Installation\n\n* Add the dependency to your environment:\n\n  ```\n  pip install vmigration-helper\n  ```\n\n* Add the app `vmgration_helper.apps.VMigrationHelperConfig` to your list of installed apps in your settings:\n\n  ```\n  INSTALLED_APPS = [\n    ...\n    \'vmigration_helper.apps.VMigrationHelperConfig\',\n    ...\n  ]\n  ```\n\n\n## Commands\n\n### migration_records\n\nShows existing migration records in your `django_migration` table.\n\n#### Optional parameters:\n\n  * `--format (console | csv)` print the info in CSV or friendlier console format (default)\n\n```\n> python manage.py migration_records --format csv\nID,Applied,App,Name\n175,2021-06-13T20:41:28.683900+00:00,contenttypes,0001_initial\n176,2021-06-13T20:41:28.717886+00:00,auth,0001_initial\n177,2021-06-13T20:41:28.742930+00:00,admin,0001_initial\n178,2021-06-13T20:41:28.761938+00:00,admin,0002_logentry_remove_auto_add\n179,2021-06-13T20:41:28.770319+00:00,admin,0003_logentry_add_action_flag_choices\n180,2021-06-13T20:41:28.791287+00:00,contenttypes,0002_remove_content_type_name\n...\n192,2021-06-13T20:41:28.991814+00:00,sessions,0001_initial\n```\n\nThese are the records of migrations applied. The fields indicate:\n  * ID - the ID of the record\n  * Applied - when the migration was applied \n  * App - name of the Django app\n  * Name - name of the migration \n\n\n### migration_current\n\nShows the ID of the latest migration record in your `django_migration` table.\n\n```\n> python manage.py migration_current_id\n192\n```\n\n192 is the ID of the latest record as shown above.\n\n### migration_rollback\n\nRoll-back (unapply) previously applied migrations _after_ (but not including) the migration ID provided.\n\n```\n> python manage.py migrateion_rollback 176\n```\n\nThe above will rollback migrations after `0001_initial` of the `auth` app:\n\n```\npython manage.py migrate sessions zero\nOperations to perform:\n  Unapply all migrations: sessions\nRunning migrations:\n  Rendering model states... DONE\n  Unapplying sessions.0001_initial... OK\n\npython manage.py migrate auth 0001_initial\nOperations to perform:\n  Target specific migration: 0001_initial, from auth\nRunning migrations:\n  Rendering model states... DONE\n  Unapplying auth.0012_alter_user_first_name_max_length... OK\n  Unapplying auth.0011_update_proxy_permissions... OK\n  Unapplying auth.0010_alter_group_name_max_length... OK\n  Unapplying auth.0009_alter_user_last_name_max_length... OK\n  Unapplying auth.0008_alter_user_username_max_length... OK\n  Unapplying auth.0007_alter_validators_add_error_messages... OK\n  Unapplying auth.0006_require_contenttypes_0002... OK\n  Unapplying auth.0005_alter_user_last_login_null... OK\n  Unapplying auth.0004_alter_user_username_opts... OK\n  Unapplying auth.0003_alter_user_email_max_length... OK\n  Unapplying auth.0002_alter_permission_name_max_length... OK\n\npython manage.py migrate contenttypes 0001_initial\nOperations to perform:\n  Target specific migration: 0001_initial, from contenttypes\nRunning migrations:\n  Rendering model states... DONE\n  Unapplying contenttypes.0002_remove_content_type_name... OK\n\npython manage.py migrate admin zero\nOperations to perform:\n  Unapply all migrations: admin\nRunning migrations:\n  Rendering model states... DONE\n  Unapplying admin.0003_logentry_add_action_flag_choices... OK\n  Unapplying admin.0002_logentry_remove_auto_add... OK\n  Unapplying admin.0001_initial... OK\n```\n\n#### Optional parameters:\n\n  * `--dry-run` will print the commands but will not actually run them\n  * `--migrate-cmd <command to run migrations>` sets the command to run migrations with. The command must accept \n    the app and migration name as the `{app}` and `{name}` placeholders, respectively.  \n    \n    For example:\n    \n    ```\n    --migrate-cmd "pipenv run python manage.py migrate {app} {name}" \n    ```\n    \n    can be used to have the command run migrations using `pipenv`.\n\n    For example:\n\n    ```\n    > pipenv run python manage.py migration_rollback 0 --dry-run --migrate-cmd "pipenv run python manage.py migrate {app} {name}"\n    pipenv run python manage.py migrate sessions zero\n    pipenv run python manage.py migrate auth 0001_initial\n    pipenv run python manage.py migrate contenttypes 0001_initial\n    pipenv run python manage.py migrate admin zero\n    pipenv run python manage.py migrate auth zero\n    pipenv run python manage.py migrate contenttypes zero\n    ```\n',
    'author': 'bluedenim',
    'author_email': 'vancly@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bluedenim/vmigration-helper',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.0,<4.0',
}


setup(**setup_kwargs)
