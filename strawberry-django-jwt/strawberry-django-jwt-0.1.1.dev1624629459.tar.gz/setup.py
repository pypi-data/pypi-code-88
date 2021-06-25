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
 'PyJWT>=1.7.1,<2.0.0',
 'django-admin-display>=1.3.0,<2.0.0',
 'strawberry-graphql-django>=0.2.2,<0.3.0',
 'strawberry-graphql>=0.64.4,<0.65.0']

setup_kwargs = {
    'name': 'strawberry-django-jwt',
    'version': '0.1.1.dev1624629459',
    'description': 'Strawberry-graphql port of the graphene-django-jwt package',
    'long_description': '# Strawberry Django JWT\n\n[![PyPI - Downloads](https://img.shields.io/pypi/dm/strawberry-django-jwt?style=for-the-badge)](https://pypi.org/project/strawberry-django-jwt/)\n\n[![GitHub commit activity](https://img.shields.io/github/commit-activity/m/KundaPanda/strawberry-django-jwt?style=for-the-badge)](https://github.com/KundaPanda/strawberry-django-jwt/graphs/commit-activity)\n![GitHub last commit](https://img.shields.io/github/last-commit/KundaPanda/strawberry-django-jwt?style=for-the-badge)\n\n![Codecov](https://img.shields.io/codecov/c/github/KundaPanda/strawberry-django-jwt?style=for-the-badge)\n[![Codacy grade](https://img.shields.io/codacy/grade/aa892e1ed8924429af95d9eeaa495338?style=for-the-badge)](https://www.codacy.com/gh/KundaPanda/strawberry-django-jwt/dashboard?utm_source=github.com&utm_medium=referral&utm_content=KundaPanda/strawberry-django-jwt&utm_campaign=Badge_Grade)\n\n[JSON Web Token](https://jwt.io/>) authentication\nfor [Strawberry Django GraphQL](https://strawberry.rocks/docs/integrations/django)\n\n---\n\n## Disclaimer\n\nThis project is a forked version of [Django GraphQL JWT](https://github.com/flavors/django-graphql-jwt) that\nsubstitutes [Graphene](https://graphene-python.org/) GraphQL backend for [Strawberry](https://strawberry.rocks/)\n\n---\n\n## Installation\n\n1. Install last stable version from Pypi:\n\n   ```shell\n   pip install strawberry-django-jwt\n   ```\n\n2. Add `AuthenticationMiddleware` middleware to your **MIDDLEWARE** settings:\n\n   ```python\n   MIDDLEWARE = [\n       ...,\n       \'django.contrib.auth.middleware.AuthenticationMiddleware\',\n       ...,\n   ]\n   ```\n\n3. Add `JSONWebTokenMiddleware` or `AsyncJSONWebTokenMiddleware` middleware to your **STRAWBERRY** schema definition:\n\n   ```python\n   from strawberry_django_jwt.middleware import JSONWebTokenMiddleware, AsyncJSONWebTokenMiddleware\n   from strawberry import Schema\n\n   schema = Schema(...)\n   schema.middleware.extend([\n        # !! IMPORTANT !!\n        # Pick only one, async middleware is needed when using AsyncGraphQLSchema\n        JSONWebTokenMiddleware(),\n        AsyncJSONWebTokenMiddleware(),\n   ])\n   ```\n\n4. Add `JSONWebTokenBackend` backend to your **AUTHENTICATION_BACKENDS**:\n\n   ```python\n   AUTHENTICATION_BACKENDS = [\n       \'strawberry_django_jwt.backends.JSONWebTokenBackend\',\n       \'django.contrib.auth.backends.ModelBackend\',\n   ]\n   ```\n\n5. Add _strawberry-django-jwt_ mutations to the root schema:\n\n   ```python\n   import strawberry\n   import strawberry_django_jwt.mutations as jwt_mutations\n\n   @strawberry.type\n   class Mutation:\n       token_auth = jwt_mutations.ObtainJSONWebToken.obtain\n       verify_token = jwt_mutations.Verify.verify\n       refresh_token = jwt_mutations.Refresh.refresh\n       delete_token_cookie = jwt_mutations.DeleteJSONWebTokenCookie.delete_cookie\n\n\n   schema = strawberry.Schema(mutation=Mutation, query=...)\n   ```\n\n6. \\[OPTIONAL\\] Set up the custom Strawberry views\n\n   These views set the status code of failed authentication attempts to 401 instead of the default 200.\n\n   ```python\n   from django.urls import re_path\n   from strawberry_django_jwt.decorators import jwt_cookie\n   from strawberry_django_jwt.views import StatusHandlingGraphQLView as GQLView\n   from ... import schema\n\n   urlpatterns += \\\n    [\n        re_path(r\'^graphql/?$\', jwt_cookie(GQLView.as_view(schema=schema))),\n    ]\n   ```\n\n   or, for async views:\n\n   ```python\n   from django.urls import re_path\n   from strawberry_django_jwt.decorators import jwt_cookie\n   from strawberry_django_jwt.views import AsyncStatusHandlingGraphQLView as AGQLView\n   from ... import schema\n\n   urlpatterns += \\\n    [\n        re_path(r\'^graphql/?$\', jwt_cookie(AGQLView.as_view(schema=schema))),\n    ]\n   ```\n\n---\n\n## Quickstart Documentation\n\n===============_Work in Progress_===============\n\nRelay support has been temporarily removed due to lack of experience with Relay\n\nMost of the features are conceptually the same as those provided\nby [Django GraphQL JWT](https://github.com/flavors/django-graphql-jwt)\n\n### Authenticating fields\n\nFields can be set to auth-only using the `login_required` decorator in combination with `strawberry.field` or\nvia `login_field`\n\n```python\nimport strawberry\nfrom strawberry.types import Info\nfrom strawberry_django_jwt.decorators import login_required\n\n\ndef auth_field(fn=None):\n    return strawberry.field(login_required(fn))\n\n\n@strawberry.type\nclass Query:\n    @auth_field\n    def hello(self, info: Info) -> str:\n        return "World"\n\n    @strawberry.field\n    @login_required\n    def foo(self, info: Info) -> str:\n        return "Bar"\n```\n\nPlease note the info argument, without which strawberry would not provide the context info required for authentication.\n\n### Mixin info injection\n\nAn alternative approach to this problem is following:\n\n```python\nimport strawberry\nfrom strawberry.types import Info\nfrom strawberry_django_jwt.decorators import login_required, login_field\nfrom strawberry_django_jwt.mixins import RequestInfoMixin\n\n\n@strawberry.type\nclass Query(RequestInfoMixin):\n    @login_field\n    def hello(self) -> str:\n        # self == { \'info\': ... } in this case\n        return "World"\n\n    @strawberry.field\n    @login_required\n    def foo(self) -> str:\n        # self == { \'info\': ... } in this case\n        return self.get("info").field_name\n\n    @strawberry.field\n    @login_required\n    def explicit_foo(self, info: Info) -> str:\n        # self == { } in this case\n        return info.field_name\n```\n\n`RequestInfoMixin` automatically injects info arguments to all fields in the class.\n\nAll function arguments that are not present in the definition will be added by the `login_required` decorator to\nthe `self` dictionary as kwargs.\n\n### Model mutations\n\nYou can add the login_required decorator to them as well\n\n```python\nimport strawberry\nfrom strawberry_django_jwt.decorators import login_required\nfrom strawberry_django_jwt.mixins import RequestInfoMixin\nfrom strawberry.django import mutations\n\n\n@strawberry.type\nclass Mutation(RequestInfoMixin):\n    foo_create: FooType = login_required(mutations.create(FooInput))\n    foo_delete: FooType = login_required(mutations.update(FooPartialInput))\n    foo_update: FooType = login_required(mutations.delete())\n```\n\n### Async views\n\nShould be fully supported :)\n\n```python\nimport strawberry\nfrom strawberry_django_jwt.decorators import login_field\nfrom strawberry_django_jwt.mixins import RequestInfoMixin\n\n\n@strawberry.type\nclass Query(RequestInfoMixin):\n    @login_field\n    async def foo(self) -> str:\n        return "bar"\n```\n',
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
