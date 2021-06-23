# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['automapper']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-automapper',
    'version': '0.0.1',
    'description': 'Library for automatically mapping one object to another',
    'long_description': '# py-automapper\nPython object auto mapper\n\nTODO:\n* use custom exception type\n* use https://docs.readthedocs.io/en/stable/index.html\n* configure poetry for building a package: https://python-poetry.org/docs/pyproject/\n* using TortoiseORM as an example of package building: https://github.com/tortoise/tortoise-orm/blob/develop\n\n\nRequirements:\n```python\nfrom automapper import mapper\n\nmapper.register_cls_extractor(ParentClassA, fields_name_extractor_function)\n\nmapper.add(ClassA, ClassB)\n\n# output type is known from registered before\nmapper.map(obj)\n\n# output type specified\nmapper.to(TargetClass).map(obj)\n\n# TODO: extra mappings, they override default mapping from `obj`\nmapper.map(obj, field1=value1, field2=value2)\n\n# TODO: same extra mappings with specific type, field1 and field2 coming from SpecificType\nmapper.map(obj, SpecificType, field1=value1, field2=value2)\n\n# TODO: don\'t map None values, by default skip_none_values == False\nmapper.map(obj, skip_none_values = True)\n\n# TODO: Mapping should be recursive\n# TODO: Add optional dependencies for \n\n# TODO: Advanced: multiple from classes\nmapper.add(FromClassA, FromClassB, ToClassC)\n\n# TODO: Advanced: add custom mappings for fields\nmapper.add(ClassA, ClassB, {"ClassA.field1", "ClassB.field2", "ClassA.field2", "ClassB.field1"})\n\n# TODO: Advanced: map multiple objects to output type\nmapper.multimap(obj1, obj2)\nmapper.to(TargetType).multimap(obj1, obj2)\n\n# TODO: Advanced: Verify correctness of all mappings and if it\'s possible to construct object\n\n```',
    'author': 'Andrii Nikolaienko',
    'author_email': 'anikolaienko14@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/anikolaienko/py-automapper',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
