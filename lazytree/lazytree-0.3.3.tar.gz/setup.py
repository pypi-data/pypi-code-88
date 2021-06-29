# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lazytree']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.0.0,<22.0.0', 'funcy>=1.12,<2.0']

setup_kwargs = {
    'name': 'lazytree',
    'version': '0.3.3',
    'description': 'Python library for manipulating infinite trees.',
    'long_description': '# Lazy Tree\n\n[![Build Status](https://cloud.drone.io/api/badges/mvcisback/pyLazyTree/status.svg)](https://cloud.drone.io/mvcisback/pyLazyTree)\n[![codecov](https://codecov.io/gh/mvcisback/DiscreteSignals/branch/master/graph/badge.svg)](https://codecov.io/gh/mvcisback/pyLazyTree)\n[![PyPI version](https://badge.fury.io/py/lazytree.svg)](https://badge.fury.io/py/lazytree)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n\n<!-- markdown-toc start - Don\'t edit this section. Run M-x markdown-toc-generate-toc again -->\n**Table of Contents**\n\n- [Installation](#installation)\n- [Usage](#usage)\n\n<!-- markdown-toc end -->\n\n\n# Installation\n\nIf you just need to use `lazytree`, you can just run:\n\n`$ pip install lazytree`\n\nFor developers, note that this project uses the\n[poetry](https://poetry.eustace.io/) python package/dependency\nmanagement tool. Please familarize yourself with it and then\nrun:\n\n`$ poetry install`\n\n# Usage\n\nA `LazyTree` is a triple, `(root, child_map, view)` where `root : A`\nand a child map, `child_map`, which maps `a` to a (finite) list of\nchildren `child_map : A -> List[A]` define the tree\'s structure and\n`view : A -> B` defines what the tree represents. The default view is\nthe identity map, `lambda x: x`.\n\nThis structure is useful for modeling infinite (or really large) trees\nwhere only a finite number of nodes need to be accessed. For example,\nthe following Binary tree represents the recursive subdivision of the\ninterval [0, 1].\n\n```python\nfrom lazytree import LazyTree\n\ndef split(itvl):\n    lo, hi = itvl\n    mid = lo + (hi - lo)/2\n    return (lo, mid), (mid, hi)\n\ntree = LazyTree(\n    root=(0, 1),  # Initial Itvl\n    child_map=split  # Itvl -> [Itvl]\n)\n```\n\nConceptually a `LazyTree` object can be thought of as containing the pieces of data.\n\n1. The `root` of the tree.\n2. The data represented by the `root`, accessed via the `view` method.\n3. The child subtrees - computed using `child_map` and accessed through the `.children` attribute.\n\nFor example, in our interval example, each node corresponds to an interval of `(0, 1)` and has two child subtrees.\n\n```python\n# View the current root.\nassert tree.view() == tree.root\n\nsubtrees = tree.children\nassert len(subtrees) == 2\n```\n\nOften, for each node in a tree, one is interested in computing a particular function. This can be done using the `map` and `view` methods. For example, below `map` each interval in the tree to it\'s size. This results in a new `LazyTree` object.\n\n```python\ntree2 = tree.map(lambda itvl: itvl[1] - itvl[0])  # Change view to itvl size.\nassert tree2.view() == 1\n\n# Access the root\'s subtrees\nsubtrees = tree2.children\nassert len(subtrees) == 2\nassert subtrees[0].root == (0, 0.5)\nassert subtrees[0].view() == 0.5\n```\n\nTravesals of a `LazyTree` object are also implemented. For example,\n\n```python\n# Breadth First Search through tree.\n## Note: calls .view() before returning. \nitvls = tree.bfs()  # returns a generator.\nsizes = tree2.bfs()  # returns a generator.\n\nassert next(itvls) == (0, 1)\nassert next(sizes) == 1\n\nassert next(itvls) == (0, 0.5)\nassert next(sizes) == 0.5\n\nassert next(itvls) == (0.5, 1)\nassert next(sizes) == 0.5\n\n# Cost guided traversal.\n## Note: Smaller means higher priority.\nsizes = tree2.cost_guided_refinement(cost=lambda x: x)\nassert next(sizes)  == 1  # (0, 1)\nassert next(sizes)  == 0.5  # (0, 0.5)\nassert next(sizes)  == 0.25  # (0, 0.25)\n\n# Iterative Deepening Depth First Traversal\nsizes = tree2.iddfs(max_depth=3)  # returns a generator.\nassert list(sizes) == [1, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125]\n\n# Note, you can reset the current view.\ntree3 = tree2.with_identity_view()\nassert tree3.view() == tree.view()\n```\n\nFinally, one can "prune" away subtrees by labeling them as leaf nodes using the `prune` method. If you are sure that the resulting tree is finite (either due to pruning or the provided `child_map`) then one can compute the leaves of the tree.\n\n```python\n# Prune subtrees with a root of size less than 0.1.\ntree4 = tree2.prune(isleaf=lambda s: s < 0.2)\nsizes = tree.bfs()\nassert all(s > 0.001 for s in sizes)  # Note that sizes is now finite.\n\n\n\n# Compute leafs of tree. Careful! Could be infinite!\nassert all(s == 0.125 for s in tree4.leaves())\nassert len(list(tree4.leaves())) == 8\n```\n',
    'author': 'Marcell Vazquez-Chanlatte',
    'author_email': 'marcell.vc@eecs.berkeley.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mvcisback/pyLazyTree',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
