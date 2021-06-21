# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['atom2vec']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.3,<2.0.0',
 'pymatgen>=2022.0.8,<2023.0.0',
 'scipy>=1.7.0,<2.0.0',
 'sklearn>=0.0,<0.1',
 'tqdm>=4.61.1,<5.0.0']

setup_kwargs = {
    'name': 'atom2vec',
    'version': '1.0.5',
    'description': 'A python implement of Atom2Vec: a simple way to describe atoms for machine learning',
    'long_description': '# Atom2Vec\nA python implement of Atom2Vec: a simple way to describe atoms for machine learning\n\n(*Updated 06/21/2021*: We refactored the code with `pymatgen`, you can find old version in branch `old_version`. Now the code is fully typed and tested.)\n## Background\nAtom2Vec is first proposed on [Zhou Q, Tang P, Liu S, et al. Learning atoms for materials discovery[J]. Proceedings of the National Academy of Sciences, 2018, 115(28): E6411-E6417.](https://www.pnas.org/content/115/28/E6411#page)\n\n## Demo\n[![Atom Similarity Demo](docs/atom_sim_vis.png)](https://old.yuxingfei.com/src/similarity.html)\n\n## Installation\n```shell\npip install atom2vec\n```\n\n## Usage\n### Generating atom vectors and atom similarity matrix\nWe use `pymatgen.core.Structure` to store all the structures. \n```python\nfrom atom2vec import AtomSimilarity\nfrom pymatgen.core import Structure\nfrom typing import List\n\nstructures: List[Structure]\natom_similarity = AtomSimilarity.from_structures(structures, \n                                                 k_dim=100, max_elements=3)\n```\n\n### Query atom vectors\n```python\nfrom atom2vec import AtomSimilarity\nfrom pymatgen.core import Element\nfrom typing import List\n\natom_similarity: AtomSimilarity\natom_vector: List[float]\n\natom_vector = atom_similarity.get_atom_vector(1)  # atomic index\natom_vector = atom_similarity.get_atom_vector("H")  # atom\'s name\natom_vector = atom_similarity.get_atom_vector(Element("H"))  # pymatgen Element Enum\n```\n\n### Query atom similarity\n```python\nfrom atom2vec import AtomSimilarity\nfrom pymatgen.core import Element\n\natom_similarity: AtomSimilarity\nsimilarity: float\n\nsimilarity = atom_similarity["Ca", "Sr"]\n```\n',
    'author': 'idocx',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/idocx/Atom2Vec',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)
