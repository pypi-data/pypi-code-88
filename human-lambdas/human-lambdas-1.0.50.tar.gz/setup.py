# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['human_lambdas',
 'human_lambdas.data_handler',
 'human_lambdas.data_handler.tests',
 'human_lambdas.external',
 'human_lambdas.external.migrations',
 'human_lambdas.external.tests',
 'human_lambdas.hl_rest_api',
 'human_lambdas.metrics',
 'human_lambdas.metrics.tests',
 'human_lambdas.organization_handler',
 'human_lambdas.organization_handler.tests',
 'human_lambdas.templates_handler',
 'human_lambdas.templates_handler.tests',
 'human_lambdas.user_handler',
 'human_lambdas.user_handler.management.commands',
 'human_lambdas.user_handler.migrations',
 'human_lambdas.user_handler.tests',
 'human_lambdas.v1',
 'human_lambdas.workflow_handler',
 'human_lambdas.workflow_handler.management.commands',
 'human_lambdas.workflow_handler.migrations',
 'human_lambdas.workflow_handler.tests']

package_data = \
{'': ['*'],
 'human_lambdas.user_handler': ['templates/*'],
 'human_lambdas.workflow_handler.tests': ['data/*', 'data/encodings/*']}

install_requires = \
['Django==2.2.13',
 'PyJWT==1.7.1',
 'analytics-python==1.2.9',
 'cchardet==0.3.5',
 'click==7.1.2',
 'django-cors-headers==3.6.0',
 'django-next-prev>=1.1.0,<2.0.0',
 'django-rest-hooks-tmp==1.6.1',
 'djangorestframework-simplejwt==4.3.0',
 'djangorestframework==3.12.2',
 'drf-chunked-upload==0.4.2',
 'drf-yasg2>=1.19.4,<2.0.0',
 'email-validator==1.1.1',
 'google-auth==1.24.0',
 'google-cloud-storage==1.36.0',
 'gunicorn==20.0.04',
 'psycopg2-binary>=2.8.6,<2.9.0',
 'python-dotenv>=0.17.1,<0.18.0',
 'requests>=2.25.1,<3.0.0',
 'schema==0.7.2',
 'sendgrid==6.4.8',
 'sentry-sdk==0.19.5',
 'typing-extensions==3.7.4',
 'whitenoise>=5.2.0,<6.0.0']

entry_points = \
{'console_scripts': ['hl = human_lambdas.hl_cli:cli',
                     'human-lambdas = human_lambdas.hl_cli:cli']}

setup_kwargs = {
    'name': 'human-lambdas',
    'version': '1.0.50',
    'description': 'Open Source Human in the Loop platform for anyone to run their own private Mechanical Turk.',
    'long_description': None,
    'author': 'Human Lambdas Ltd.',
    'author_email': 'bernat@humanlambdas.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Human-Lambdas/human-lambdas',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
