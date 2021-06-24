from setuptools import setup

name = "types-pathlib2"
description = "Typing stubs for pathlib2"
long_description = '''
## Typing stubs for pathlib2

This is an auto-generated PEP 561 type stub package for `pathlib2` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `pathlib2`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/pathlib2. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `bda76bb7d8bcf97e67f50e3650ae5e9fb8d896aa`.
'''.lstrip()

setup(name=name,
      version="0.1.6",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['pathlib2-python2-stubs'],
      package_data={'pathlib2-python2-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
