from setuptools import setup

name = "types-MarkupSafe"
description = "Typing stubs for MarkupSafe"
long_description = '''
## Typing stubs for MarkupSafe

This is an auto-generated PEP 561 type stub package for `MarkupSafe` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `MarkupSafe`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/MarkupSafe. All fixes for
types and metadata should be contributed there.

*Note:* The `MarkupSafe` package includes type annotations or type stubs
since version 2.0. Please uninstall the `types-MarkupSafe`
package if you use this or a newer version.


See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `50f5858a5628529b7a453c675e0f4b1eeccc704d`.
'''.lstrip()

setup(name=name,
      version="1.1.4",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['markupsafe-stubs'],
      package_data={'markupsafe-stubs': ['_native.pyi', '_constants.pyi', '_compat.pyi', '_speedups.pyi', '__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
