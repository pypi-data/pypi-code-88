# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagviz', 'dagviz.style']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.5.1,<3.0.0', 'svgwrite>=1.4.1,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.0,<2.0']}

setup_kwargs = {
    'name': 'dagviz',
    'version': '0.2.0',
    'description': 'Visualization for DAGs',
    'long_description': '# DAGVIZ\nDAGVIZ offers a "git log"-like visualization for DAGs represented in networkx.\n\n## Installation\n\nDAGVIZ can be installed with `pip`:\n\n```bash\npip install dagviz\n```\n\n## Documentation\n\nDocumentation is available at https://wimyedema.github.io/dagviz/.\n## Usage\n\nDAGVIZ relies on networkx for the representation and manipulation of the\nDAG. An SVG file can be generated as follows:\n\n```py\n    import dagviz\n    import networkx as nx\n    # Create the DAG\n    G = nx.DiGraph()\n    for i in range(5):\n        G.add_node(f"n{i}")\n    G.add_edge(f"n0", f"n1")\n    G.add_edge(f"n0", f"n2")\n    G.add_edge(f"n0", f"n4")\n    G.add_edge(f"n1", f"n3")\n    G.add_edge(f"n2", f"n3")\n    G.add_edge(f"n3", f"n4")\n    # Create an SVG as a string\n    r = dagviz.render_svg(G)\n    with open("simple.svg", "wt") as fs:\n        fs.write(r)\n```\n',
    'author': 'Wim Yedema',
    'author_email': 'wim.yedema@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/WimYedema/dagviz.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
