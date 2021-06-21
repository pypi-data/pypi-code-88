from setuptools import setup

name = "types-kazoo"
description = "Typing stubs for kazoo"
long_description = '''
## Typing stubs for kazoo

This is an auto-generated PEP 561 type stub package for `kazoo` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `kazoo`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/kazoo. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `3ec061022af0c313761e0ac65c59718466bf67cb`.
'''.lstrip()

setup(name=name,
      version="0.1.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['kazoo-python2-stubs'],
      package_data={'kazoo-python2-stubs': ['client.pyi', 'exceptions.pyi', '__init__.pyi', 'recipe/watchers.pyi', 'recipe/__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
