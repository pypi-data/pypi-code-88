from setuptools import setup

name = "types-Markdown"
description = "Typing stubs for Markdown"
long_description = '''
## Typing stubs for Markdown

This is an auto-generated PEP 561 type stub package for `Markdown` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `Markdown`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/Markdown. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `a319ba46049585862511ee049e02008cced4cfc3`.
'''.lstrip()

setup(name=name,
      version="3.3.0",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      install_requires=[],
      packages=['markdown-stubs'],
      package_data={'markdown-stubs': ['postprocessors.pyi', '__meta__.pyi', 'blockprocessors.pyi', 'core.pyi', 'pep562.pyi', 'util.pyi', 'treeprocessors.pyi', 'blockparser.pyi', 'preprocessors.pyi', '__init__.pyi', 'inlinepatterns.pyi', 'serializers.pyi', 'extensions/legacy_attrs.pyi', 'extensions/sane_lists.pyi', 'extensions/md_in_html.pyi', 'extensions/codehilite.pyi', 'extensions/extra.pyi', 'extensions/legacy_em.pyi', 'extensions/footnotes.pyi', 'extensions/fenced_code.pyi', 'extensions/wikilinks.pyi', 'extensions/admonition.pyi', 'extensions/smarty.pyi', 'extensions/meta.pyi', 'extensions/toc.pyi', 'extensions/def_list.pyi', 'extensions/attr_list.pyi', 'extensions/__init__.pyi', 'extensions/tables.pyi', 'extensions/abbr.pyi', 'extensions/nl2br.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Typing :: Typed",
      ]
)
