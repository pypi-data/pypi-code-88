# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_rest']

package_data = \
{'': ['*']}

install_requires = \
['fastapi', 'tortoise-orm']

setup_kwargs = {
    'name': 'fastapi-rest',
    'version': '0.1.1',
    'description': 'Fast restful API based on FastAPI and TortoiseORM',
    'long_description': '# fastapi-rest\n\n[![image](https://img.shields.io/pypi/v/fastapi-rest.svg?style=flat)](https://pypi.python.org/pypi/fastapi-rest)\n[![image](https://img.shields.io/github/license/long2ice/fastapi-rest)](https://github.com/long2ice/fastapi-rest)\n[![image](https://github.com/long2ice/fastapi-rest/workflows/pypi/badge.svg)](https://github.com/long2ice/fastapi-rest/actions?query=workflow:pypi)\n[![image](https://github.com/long2ice/fastapi-rest/workflows/ci/badge.svg)](https://github.com/long2ice/fastapi-rest/actions?query=workflow:ci)\n\n## Introduction\n\nFast restful API based on FastAPI and TortoiseORM.\n\n## Install\n\n```shell\npip install fastapi-rest\n```\n\n## Quick Start\n\nFirst, define your `ListView` resource.\n\n```python\nfrom fastapi_rest.resource import ListView\n\n\nclass UserList(ListView):\n    model = User\n    fields = ("name", "age")\n```\n\nSecond, include router to your app.\n\n```python\napp.include_router(UserList.as_router())\n```\n\nNow, you can visit the endpoint `/user` to get user list.\n\n### ListView\n\nExport the endpoint `GET /{resource}`.\n\n```python\nclass ListView(Resource):\n    paginator: Paginator = Paginator()\n    fields: Optional[Tuple[str, ...]] = None\n    exclude: Optional[Tuple[str, ...]] = None\n    queryset: Optional[QuerySet] = None\n    query: Optional[Type[BaseModel]] = None\n```\n\n### DetailView\n\nExport the endpoint `GET /{resource}/{pk}`.\n\n```python\nclass DetailView(Resource):\n    fields: Optional[Tuple[str, ...]] = None\n    exclude: Optional[Tuple[str, ...]] = None\n```\n\n### CreateView\n\nExport the endpoint `POST /{resource}`.\n\n```python\nclass CreateView(Resource):\n    schema: Optional[Type[BaseModel]] = None\n```\n\n### UpdateView\n\nExport the endpoint `PUT /{resource}/{pk}`.\n\n```python\nclass UpdateView(Resource):\n    schema: Type[BaseModel]\n```\n\n### DeleteView\n\nExport the endpoint `DELETE /{resource}/{pk}`.\n\n```python\nclass DeleteView(Resource):\n    pass\n```\n\n## Reference\n\nYou can see the examples [here](./examples).\n\n## License\n\nThis project is licensed under the [Apache2.0](https://github.com/long2ice/fastapi-rest/blob/master/LICENSE) License.\n',
    'author': 'long2ice',
    'author_email': 'long2ice@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/long2ice/fastapi-rest',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
