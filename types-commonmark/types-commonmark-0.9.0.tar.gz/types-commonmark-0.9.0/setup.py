from setuptools import setup

name = "types-commonmark"
description = "Typing stubs for commonmark"
long_description = '''
## Typing stubs for commonmark

This is an auto-generated PEP 561 type stub package for `commonmark` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `commonmark`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/commonmark. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `1cffceb767ea0da01b4d03cce8d97f9bbe3d08b3`.
'''.lstrip()

setup(name=name,
      version="0.9.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['commonmark-stubs'],
      package_data={'commonmark-stubs': ['inlines.pyi', 'dump.pyi', 'cmark.pyi', 'entitytrans.pyi', 'main.pyi', 'normalize_reference.pyi', 'blocks.pyi', 'common.pyi', '__init__.pyi', 'node.pyi', 'render/html.pyi', 'render/rst.pyi', 'render/__init__.pyi', 'render/renderer.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
