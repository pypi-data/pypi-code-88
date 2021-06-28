# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['speccify']

package_data = \
{'': ['*']}

install_requires = \
['djangorestframework',
 'djangorestframework-dataclasses',
 'drf-spectacular',
 'typing-extensions']

setup_kwargs = {
    'name': 'speccify',
    'version': '0.1.1',
    'description': 'Tie together `drf-spectacular` and `djangorestframework-dataclasses` for easy-to-use apis and openapi schemas.',
    'long_description': '# Speccify\n\nTie together `drf-spectacular` and `djangorestframework-dataclasses` for\neasy-to-use apis and openapi schemas.\n\n## Usage\n\n```\n    @dataclass\n    class MyQueryData():\n        name: str\n\n    @dataclass\n    class MyResponse:\n        length: int\n\n    @speccify.api_view(methods=["GET"], permissions=[])\n    def my_view(request: Request, my_query: Query[MyQueryData]) -> MyResponse:\n        name = my_query.name\n        length = len(name)\n        return MyResponse(length=length)\n```\n\n\n## License\n\nApache2\n',
    'author': 'Lyst Ltd.',
    'author_email': 'devs@lyst.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
