# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pandas_genomics',
 'pandas_genomics.accessors',
 'pandas_genomics.accessors.utils',
 'pandas_genomics.arrays',
 'pandas_genomics.io',
 'pandas_genomics.io.plink',
 'pandas_genomics.sim']

package_data = \
{'': ['*']}

install_requires = \
['numpy==1.18',
 'pandas>=1.2,<2.0',
 'scipy>=1.6,<1.7',
 'statsmodels>=0.12.2,<0.13.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=2.0,<3.0'],
 ':sys_platform != "win32"': ['cyvcf2>=0.20.9,<0.21.0'],
 'docs': ['sphinx>=3.2.1,<4.0.0',
          'sphinx_rtd_theme>=0.5.0,<0.6.0',
          'numpydoc>=1.1.0,<2.0.0',
          'sphinx-copybutton>=0.3.0,<0.4.0',
          'ipython>=7.18.1,<8.0.0']}

setup_kwargs = {
    'name': 'pandas-genomics',
    'version': '0.5.0',
    'description': 'Pandas ExtensionDtypes and ExtensionArray for working with genomics data',
    'long_description': '<div align="center">\n<img src="https://github.com/HallLab/pandas-genomics/raw/master/docs/_static/logo.png" alt="pandas_genomics logo"/>\n</div>\n\n<br/>\n\n<div align="center">\n\n<!-- Python version -->\n<a href="https://pypi.python.org/pypi/pandas-genomics">\n<img src="https://img.shields.io/badge/python-3.7+-blue.svg?style=flat-square" alt="PyPI version"/>\n</a>\n<!-- PyPi -->\n<a href="https://pypi.org/project/pandas-genomics/">\n<img src="https://img.shields.io/pypi/v/pandas-genomics.svg?style=flat-square" alt="pypi" />\n</a><br>\n<!-- Build status -->\n<a href="https://github.com/HallLab/pandas-genomics/actions?query=workflow%3ACI">\n<img src="https://img.shields.io/github/workflow/status/HallLab/pandas-genomics/CI?style=flat-square" alt="Build Status" />\n</a>\n<!-- Docs -->\n<a href="https://pandas-genomics.readthedocs.io/en/latest/">\n<img src="https://img.shields.io/readthedocs/pandas-genomics?style=flat-square" alt="Read the Docs" />\n</a>\n<!-- Test coverage -->\n<a href="https://codecov.io/gh/HallLab/pandas-genomics/">\n<img src="https://img.shields.io/codecov/c/gh/HallLab/pandas-genomics.svg?style=flat-square" alt="Coverage Status"/>\n</a><br>\n<!-- License -->\n<a href="https://opensource.org/licenses/BSD-3-Clause">\n<img src="https://img.shields.io/pypi/l/pandas-genomics?style=flat-square" alt="license"/>\n</a>\n<!-- Black -->\n<a href="https://github.com/psf/black">\n<img src="https://img.shields.io/badge/code%20style-Black-black?style=flat-square" alt="code style: black"/>\n</a>\n</div>\n\n<br/>\n\nPandas ExtensionDtypes and ExtensionArray for working with genomics data\n\nQuickstart\n----------\n\n`Variant` objects holds information about a particular variant:\n\n```python\nfrom pandas_genomics.scalars import Variant\nvariant = Variant(\'12\', 112161652, id=\'rs12462\', ref=\'A\', alt=[\'C\', \'T\'])\nprint(variant)\n```\n    rs12462[chr=12;pos=112161652;ref=A;alt=C,T]\n    \nEach variant should have a unique ID, and a random ID is generated if one is not specified.\n\n`Genotype` objects are associated with a particular `Variant`:\n\n```python\ngt = variant.make_genotype("A", "C")\nprint(gt)\n```\n```\nA/C\n```\n\nThe `GenotypeArray` stores genotypes with an associated variant and has useful methods and properties:\n\n```python\nfrom pandas_genomics.scalars import Variant\nfrom pandas_genomics.arrays import GenotypeArray\nvariant = Variant(\'12\', 112161652, id=\'rs12462\', ref=\'A\', alt=[\'C\'])\ngt_array = GenotypeArray([variant.make_genotype_from_str(s) for s in ["C/C", "A/C", "A/A"]])\nprint(gt_array)\n```\n\n```\n<GenotypeArray>\n[Genotype(variant=rs12462[chr=12;pos=112161652;ref=A;alt=C], allele1=1, allele2=1),\nGenotype(variant=rs12462[chr=12;pos=112161652;ref=A;alt=C], allele1=0, allele2=1),\nGenotype(variant=rs12462[chr=12;pos=112161652;ref=A;alt=C], allele1=0, allele2=0)]\nLength: 3, dtype: genotype[12; 112161652; rs12462; A; C]\n```\n\n```python\nprint(gt_array.astype(str))\n```\n\n```\n    [\'C/C\' \'A/C\' \'A/A\']\n```\n\n```python\nprint(gt_array.encode_dominant())\n```\n\n```\n    <IntegerArray>\n    [1, 1, 0]\n    Length: 3, dtype: UInt8\n```\n\nThere are also `genomics` accessors for Series and DataFrame\n\n```python\nimport pandas as pd\nprint(pd.Series(gt_array).genomics.encode_codominant())\n```\n\n```\n    0    Hom\n    1    Het\n    2    Ref\n    Name: rs12462_C, dtype: category\n    Categories (3, object): [\'Ref\' < \'Het\' < \'Hom\']\n```\n',
    'author': 'John McGuigan',
    'author_email': 'jrm5100@psu.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/HallLab/pandas-genomics/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.10',
}


setup(**setup_kwargs)
