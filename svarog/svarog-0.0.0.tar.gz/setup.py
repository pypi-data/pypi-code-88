# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['svarog', 'svarog.dispatchers']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'svarog',
    'version': '0.0.0',
    'description': 'Svarog allow to create object from non typed data',
    'long_description': '======\nSvarog\n======\n\n\n.. image:: https://img.shields.io/pypi/v/svarog.svg\n        :target: https://pypi.python.org/pypi/svarog\n\n.. image:: https://img.shields.io/travis/dswistowski/svarog.svg\n        :target: https://travis-ci.com/dswistowski/svarog\n\n.. image:: https://readthedocs.org/projects/svarog/badge/?version=latest\n        :target: https://svarog.readthedocs.io/en/latest/?badge=latest\n        :alt: Documentation Status\n\n\n\n\nSvarog allow to create object from non typed data. All it need is annotated `__init__` method:\n\n\n>>> from svarog import forge\n... class A:\n...     def __init__(self, a: int, b: str):\n...       self._a = a\n...       self._b = b\n...    def __repr__(self):\n...        return f\'A(a={self._a}, b="{self._b}")\'\n>>> forge(A, {"a": 1, "b": "3"})\nA(a=1, b="3")\n\n\nMore complicated types as `Sequence`, `Mapping`, `Optional` are possible\n\n>>> class A:\n...     def __init__(self, b: Sequence[int]):\n...         self._b = b\n...     def __repr__(self):\n...         return f\'A(b={self._b})\'\n>>> forge(A, {"b": "3213"})\nA(b=[3, 2, 1, 3])\n\nYou can use forward refs:\n\n>>> class WithRef:\n...    def __init__(self, child: Optional[\'WithRef\']):\n...        self._child = child\n...    def __repr__(self):\n...        return f"WithRef({self._child!r})"\n>>> forge(WithRef(WithRef(WithRef())))\nWithRef(WithRef(WithRef(None)))\n\n\nObjects are forged recursively:\n\n\n>>> @dataclass\n... class A:\n...     b: \'B\'\n...     c: \'C\'\n... @dataclass\n... class B:\n...     number: int\n... @dataclass\n... class C:\n...     string: str\n>>> forge(A, {\'b\': {\'number\': 42}, \'c\': {\'string\': \'the-string\'}})\nA(b=B(number=42), c=C(string=\'the-string\'))\n\n\nYou can register own forge for your classes:\n\n>>> class FooType(Enum):\n...     LOREM = "lorem"\n...     IPSUM = "ipsum"\n...\n... class FooParams:\n...     types: ClassVar[Mapping[FooType, "FooParams"]] = {}\n...     def __init_subclass__(cls, type: FooType):\n...        cls.types[type] = cls\n...\n...    @classmethod\n...    def for_type(cls, type):\n...        return cls.types[type]\n...\n... @dataclass\n... class LoremFooParams(FooParams, type=FooType.LOREM):\n...     lorem: str\n...\n... @dataclass\n... class IpsumFooParams(FooParams, type=FooType.IPSUM):\n...     ipsum: int\n...\n... @dataclass\n... class Foo:\n...     type: FooType\n...     params: FooParams\n...\n...     @classmethod\n...     def forge(cls, _, data, forge):\n...         foo_type = forge(FooType, data["type"])\n...         return Foo(\n...             type=forge(FooType, foo_type),\n...             params=forge(FooParams.for_type(foo_type), data["params"])\n...         )\n...\n>>> register_forge(Foo, Foo.forge)\n>>> forge(Foo, {"type": "lorem", "params": {"lorem": "foo-bar"}})\nFoo(type=<FooType.LOREM: \'lorem\'>, params=LoremFooParams(lorem=\'foo-bar\'))\n\n>>> forge(Foo, {"type": "ipsum", "params": {"ipsum": 42}})\nFoo(type=<FooType.IPSUM: \'ipsum\'>, params=IpsumFooParams(ipsum=42))\n\n\n* Free software: MIT license\n* Documentation: https://svarog.readthedocs.io.\n\n\nFeatures\n--------\n\n* Converts unstructured data into structured recursively\n\n  * Works with `dataclasses`\n  * Works with `Sequence`, `Mapping`, `Optional`\n  * Special conventers for types can be registered with\n\nCredits\n-------\n\nSome parts of this code, and concept borrowed from cattrs_ project\n\n.. _Cattrs: https://github.com/Tinche/cattrs\n\nThis package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage\n',
    'author': 'Damian Świstowski',
    'author_email': 'damian@swistowski.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/dswistowski/svarog/',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<=3.9',
}


setup(**setup_kwargs)
