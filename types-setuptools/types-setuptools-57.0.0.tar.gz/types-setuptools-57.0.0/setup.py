from setuptools import setup

name = "types-setuptools"
description = "Typing stubs for setuptools"
long_description = '''
## Typing stubs for setuptools

This is an auto-generated PEP 561 type stub package for `setuptools` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `setuptools`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/setuptools. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `a319ba46049585862511ee049e02008cced4cfc3`.
'''.lstrip()

setup(name=name,
      version="57.0.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['pkg_resources-stubs'],
      package_data={'pkg_resources-stubs': ['py31compat.pyi', '__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
