from setuptools import setup

name = "types-redis"
description = "Typing stubs for redis"
long_description = '''
## Typing stubs for redis

This is an auto-generated PEP 561 type stub package for `redis` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `redis`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/redis. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `679ddde66edc34c33b54b0fdbc9595740eb51cd7`.
'''.lstrip()

setup(name=name,
      version="3.5.4",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['redis-stubs'],
      package_data={'redis-stubs': ['client.pyi', 'utils.pyi', 'exceptions.pyi', 'connection.pyi', 'lock.pyi', '__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
