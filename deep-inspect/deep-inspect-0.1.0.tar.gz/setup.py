# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deep_inspect']

package_data = \
{'': ['*']}

extras_require = \
{':python_version >= "3.6" and python_version < "4.0"': ['pydantic>=1.7.1,<2.0.0']}

setup_kwargs = {
    'name': 'deep-inspect',
    'version': '0.1.0',
    'description': 'A library for dynamically loading plugins',
    'long_description': 'Deep Inspect\n============\n\nDeep Inspect is a library that wraps `inspect` built-in module. It\'s purpose\nis to allow you to explore python packages in a \'deeper\' manner -\ndown to the most inner files in the package\'s hierarchy.\n\nCurrently, Deep Inspect offers `get_subclasses()` and `get_members` in a \'deeper\' manner.\n\n\nInstallation\n----------\nTo install the newest version use the following command:\n```\npip install -U deep-inspect\n```\n\n\nBasic Usage\n----------------\nIn order to find every function in `pydantic` package:\n```python\nimport inspect\n\nimport pydantic\n\nimport deep_inspect\n\nif __name__ == \'__main__\':\n    pydantic_functions = deep_inspect.get_members(pydantic, inspect.isfunction)\n    print(pydantic_functions)\n```\n\nIn order to find all subclasses of `BaseModel` in `pydantic` package:\n```python\nimport pydantic\nfrom pydantic import BaseModel\n\nimport deep_inspect\n\nif __name__ == \'__main__\':\n    base_model_subclasses = deep_inspect.get_subclasses(BaseModel, pydantic)\n    print(base_model_subclasses)\n```\n\nYou can also use the `get_subclasses()` function with a `set()` of packages:\n\n```python\nimport pydantic\nimport pytest\nfrom pydantic import BaseModel\n\nimport deep_inspect\n\nif __name__ == \'__main__\':\n    base_model_subclasses = deep_inspect.get_subclasses(BaseModel, {pydantic, pytest})\n    print(base_model_subclasses)\n```\n\n### Factory example\nOriginally, Deep Inspect goal was to implement `get_subclasses()` functions to help register `class`es\nto a Factory in a dynamic matter.\n\nRefer to the following code sample:\n```python\nfrom typing import TypeVar\n\nimport pydantic\nfrom pydantic import BaseModel\n\nimport deep_inspect\n\nK = TypeVar("K")\nV = TypeVar("V")\n\n\nclass Factory:\n    def __init__(self):\n        self.builders = {}\n\n    def register_builder(self, key: K, builder: V):\n        self.builders[key] = builder\n\n    def create(self, key: K, **kwargs):\n        builder = self.builders.get(key)\n        if not builder:\n            raise ValueError(key)\n        return builder(**kwargs)\n\n\nif __name__ == "__main__":\n    base_model_inheritors = deep_inspect.get_subclasses(BaseModel, pydantic)\n\n    factory = Factory()\n\n    # register the dynamically loaded `BaseModel` inheritors to `factory`\n    for base_model_inheritor in base_model_inheritors:\n        factory.register_builder(base_model_inheritor.__name__, base_model_inheritor)\n\n```\n\n\nContribution\n------------\n\nAs Deep Inspect started as a helper library for my current job (refer to the `Factory` example), \nit hasn\'t reached its full potential.\nYou are more than welcome to create PRs and I will review them in my free time.\n\nLinks\n-----\n- PyPI Releases: https://pypi.org/project/deep-inspect\n- PRs: https://github.com/GuyTuval/deep-inspect/pulls\n- Issue Tracker: https://github.com/GuyTuval/deep-inspect/issues\n',
    'author': 'GuyTuval',
    'author_email': 'guytuval@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/GuyTuval/loadit',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
