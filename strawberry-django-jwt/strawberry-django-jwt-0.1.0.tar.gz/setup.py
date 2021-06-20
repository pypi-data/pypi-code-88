# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['strawberry_django_jwt',
 'strawberry_django_jwt.refresh_token',
 'strawberry_django_jwt.refresh_token.admin',
 'strawberry_django_jwt.refresh_token.management',
 'strawberry_django_jwt.refresh_token.management.commands',
 'strawberry_django_jwt.refresh_token.migrations']

package_data = \
{'': ['*'],
 'strawberry_django_jwt': ['locale/ar/LC_MESSAGES/*',
                           'locale/es/LC_MESSAGES/*',
                           'locale/fr/LC_MESSAGES/*',
                           'locale/nl/LC_MESSAGES/*',
                           'locale/pt_BR/LC_MESSAGES/*'],
 'strawberry_django_jwt.refresh_token': ['locale/ar/LC_MESSAGES/*',
                                         'locale/es/LC_MESSAGES/*',
                                         'locale/fr/LC_MESSAGES/*',
                                         'locale/nl/LC_MESSAGES/*',
                                         'locale/pt_BR/LC_MESSAGES/*']}

install_requires = \
['Django>=3.0,<4.0',
 'PyJWT>=2.1.0,<3.0.0',
 'django-admin-display>=1.3.0,<2.0.0',
 'strawberry-graphql-django>=0.2.2,<0.3.0',
 'strawberry-graphql>=0.67.0,<0.68.0']

setup_kwargs = {
    'name': 'strawberry-django-jwt',
    'version': '0.1.0',
    'description': 'Strawberry-graphql port of the graphene-django-jwt package',
    'long_description': "# Strawberry Django JWT\n\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/strawberry-django-jwt?style=for-the-badge)](https://pypi.org/project/strawberry-django-jwt/)\n[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/KundaPanda/strawberry-django-jwt?style=for-the-badge)](https://github.com/KundaPanda/strawberry-django-jwt/graphs/commit-activity)\n![GitHub last commit](https://img.shields.io/github/last-commit/KundaPanda/strawberry-django-jwt?style=for-the-badge)\n\n[JSON Web Token](https://jwt.io/>) authentication\nfor [Strawberry Django GraphQL](https://strawberry.rocks/docs/integrations/django)\n\n---\n\n## Disclaimer\n\nThis project is a forked version of [Django GraphQL JWT](https://github.com/flavors/django-graphql-jwt) that substitutes [Graphene](https://graphene-python.org/) GraphQL backend for [Strawberry](https://strawberry.rocks/)\n\n---\n\n## Installation\n\n1. Install last stable version from Pypi:\n\n   ```shell\n   pip install strawberry-django-jwt\n   ```\n\n2. Add `AuthenticationMiddleware` middleware to your **MIDDLEWARE** settings:\n\n   ```python\n   MIDDLEWARE = [\n       ...,\n       'django.contrib.auth.middleware.AuthenticationMiddleware',\n       ...,\n   ]\n   ```\n\n3. Add `JSONWebTokenMiddleware` middleware to your **STRAWBERRY** schema definition:\n\n   ```python\n   from strawberry_django_jwt.middleware import JSONWebTokenMiddleware\n   from strawberry import Schema\n\n   schema = Schema(...)\n   schema.middleware.extend([\n        JSONWebTokenMiddleware(),\n   ])\n   ```\n\n4. Add `JSONWebTokenBackend` backend to your **AUTHENTICATION_BACKENDS**:\n\n   ```python\n   AUTHENTICATION_BACKENDS = [\n       'strawberry_django_jwt.backends.JSONWebTokenBackend',\n       'django.contrib.auth.backends.ModelBackend',\n   ]\n   ```\n\n5. Add _django-graphql-jwt_ mutations to the root schema:\n\n   ```python\n   import strawberry\n   import strawberry_django_jwt.mutations as jwt_mutations\n\n   @strawberry.type\n   class Mutation:\n       token_auth = jwt_mutations.ObtainJSONWebToken.obtain\n       verify_token = jwt_mutations.Verify.verify\n       refresh_token = jwt_mutations.Refresh.refresh\n\n\n   schema = strawberry.Schema(mutation=Mutation, query=...)\n   ```\n\n---\n\n## Documentation\n\n_Work in Progress_\n",
    'author': 'KundaPanda',
    'author_email': 'vojdoh@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
