from setuptools import setup

name = "types-pytz"
description = "Typing stubs for pytz"
long_description = '''
## Typing stubs for pytz

This is an auto-generated PEP 561 type stub package for `pytz` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `pytz`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/pytz. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `a319ba46049585862511ee049e02008cced4cfc3`.
'''.lstrip()

setup(name=name,
      version="2021.1.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['pytz-stubs'],
      package_data={'pytz-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
