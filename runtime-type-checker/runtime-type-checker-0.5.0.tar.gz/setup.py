# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['runtime_type_checker', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['typing_inspect>=0.7.1,<0.8.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses==0.7']}

setup_kwargs = {
    'name': 'runtime-type-checker',
    'version': '0.5.0',
    'description': 'Runtime-type-checker performs type check at runtime with help of type annotations',
    'long_description': 'runtime-type-checker\n====================\n![PyPI](https://img.shields.io/pypi/v/runtime-type-checker)\n![PyPI - License](https://img.shields.io/pypi/l/runtime-type-checker)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nThis package performs type-check at runtime with help of type annotations.\n\n## How to use this package\n\nThere are two ways to perform type checks using this package.\n\nI provide a few simple examples here. For a complete overview, have a look at the package\'s unit tests.\n\n### 1- the `check_type` function\n\nYou can check an object against a type or an annotation via the `check_type` function.\n\nThe function returns `None` if the check was successful or raises a `TypeError` in case of error.\n\nNote that this function does not check recursively for e.g. the attributes of a class.\n```python\nfrom typing import List, Sequence, Optional, Mapping\nfrom dataclasses import dataclass\nfrom runtime_type_checker import check_type\n\n\ncheck_type("a", str)  # OK\ncheck_type(["a"], List[str])  # OK\ncheck_type(["a", 1], Sequence[str])  # raises TypeError\n\n\n@dataclass\nclass Foo:\n    a: int\n    b: Optional[Mapping[str, int]] = None\n\n\ncheck_type(Foo(1), Foo)  # OK\ncheck_type(Foo(1), int)  # raises TypeError\n```\n\n### 2- The check_types decorator\n\nYou can also type-check classes upon instance creation and functions or methods upon call through the `check_types`\ndecorator:\n```python\nfrom typing import Optional, Mapping\nfrom dataclasses import dataclass\nfrom runtime_type_checker import check_types\n\ndef run_typed(f):\n  return check_types(dataclass(f))\n\n@check_types\n@dataclass\nclass Foo:\n    a: int\n    b: Optional[Mapping[str, int]] = None\n\n\nFoo(1)              # returns an instance of foo\nFoo(0, {"a": "b"})  # raises TypeError\n\n\n@check_types\ndef bar(a: bool, **options: str) -> str:\n    return options.get("b", "missing") if a else "unknown"\n\nbar(True, b="1")  # returns "1"\nbar(True, c=1)    # raises TypeError\n```\n\n## Package features and short-comings\n\n### 1- Features\n- _simplicity_: there\'s only one function and one decorator to keep in mind.\n- _robustness_: this package relies on the `typing-inspect` for the heavy lifting. This package is maintained by\ncore contributors to the typing module, which means very little hacks on my side to work with older versions of python.\n\n### 2- Short-comings\n\n- _coverage_: I don\'t offer coverage for all features of type annotations: for example Protocol, Generators, IO are not\ncurrently supported. Generics are not really well handled.\n',
    'author': 'PJCampi',
    'author_email': 'pierrejean.campigotto@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pjcampi/runtime-type-checker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
