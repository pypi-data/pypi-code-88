from setuptools import setup

name = "types-html5lib"
description = "Typing stubs for html5lib"
long_description = '''
## Typing stubs for html5lib

This is an auto-generated PEP 561 type stub package for `html5lib` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `html5lib`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/html5lib. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `f260ea238308fe9ad1b9bd57ed6b573e6b653c97`.
'''.lstrip()

setup(name=name,
      version="1.1.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['html5lib-stubs'],
      package_data={'html5lib-stubs': ['_utils.pyi', 'constants.pyi', 'html5parser.pyi', '_ihatexml.pyi', '_tokenizer.pyi', '__init__.pyi', 'serializer.pyi', '_inputstream.pyi', 'treebuilders/base.pyi', 'treebuilders/dom.pyi', 'treebuilders/etree_lxml.pyi', 'treebuilders/__init__.pyi', 'treebuilders/etree.pyi', '_trie/_base.pyi', '_trie/py.pyi', '_trie/__init__.pyi', 'treeadapters/sax.pyi', 'treeadapters/genshi.pyi', 'treeadapters/__init__.pyi', 'treewalkers/base.pyi', 'treewalkers/dom.pyi', 'treewalkers/etree_lxml.pyi', 'treewalkers/genshi.pyi', 'treewalkers/__init__.pyi', 'treewalkers/etree.pyi', 'filters/inject_meta_charset.pyi', 'filters/base.pyi', 'filters/lint.pyi', 'filters/optionaltags.pyi', 'filters/whitespace.pyi', 'filters/sanitizer.pyi', 'filters/alphabeticalattributes.pyi', 'filters/__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
