# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['scml_vis', 'scml_vis.vendor', 'scml_vis.vendor.quick']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.15.4,<6.0.0',
 'click-config-file>=0.6.0,<0.7.0',
 'click>=7.1.2,<8.0.0',
 'csvs-to-sqlite>=1.2,<2.0',
 'datasette-vega>=0.6.2,<0.7.0',
 'numpy>=1.20.2,<2.0.0',
 'pandas>=1.2.3,<2.0.0',
 'plotly>=4.14.3,<5.0.0',
 'seaborn>=0.11.1,<0.12.0',
 'streamlit>=0.80.0,<0.81.0',
 'watchdog>=2.0.2,<3.0.0']

entry_points = \
{'console_scripts': ['scml-vis = scml_vis.cli:main',
                     'scmlv = scml_vis.cli:main',
                     'scmlvis = scml_vis.cli:main']}

setup_kwargs = {
    'name': 'scml-vis',
    'version': '0.2.9',
    'description': 'A simple visualiser for SCML worlds and tournaments',
    'long_description': '# scml-vis\n\n[![ci](https://github.com/yasserfarouk/scml-vis/actions/workflows/main.yml/badge.svg)](https://github.com/yasserfarouk/scml-vis/actions/workflows/main.yml)\n[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://scml-vis.github.io/scml-vis/)\n[![pypi version](https://img.shields.io/pypi/v/scml-vis.svg)](https://pypi.org/project/scml-vis/)\n[![gitter](https://badges.gitter.im/join%20chat.svg)](https://gitter.im/scml-vis/community)\n\nA simple visualiser for SCML worlds and tournaments.\nYou can watch [a demo on YouTube](https://youtu.be/BCDjnnSmIsk)\n[![Alt text](https://img.youtube.com/vi/BCDjnnSmIsk/0.jpg)](https://youtu.be/BCDjnnSmIsk)\n<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/BCDjnnSmIsk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->\n<!--  -->\n## Screenshots\n![Screen Shot 1](docs/shot1.png)\n![Screen Shot 2](docs/shot2.png)\n\n## Main Features\n\n- Displays any world/tournament run using the [SCML package](https://www.github.com/yasserfarouk/scml)\n- Allows filtering using worlds, agent types, and agent instances\n- Shows world statistics, agent type and instance statistics and contract\n  statistics as functions of simulation step/time\n\n\n## Requirements\n\n- scml-vis requires Python 3.8 or above.\n- scml-vis can visualize worlds created by [scml](https://github.com/yasserfarouk/scml) 0.4.2 or later (simulations created using older versions of scml can be visualized in most cases but are not officially supported).\n\n## Installation\n\nWith `pip`:\n```bash\npython3 -m pip install scml-vis\n```\n\nWith [`pipx`](https://github.com/pipxproject/pipx):\n```bash\npython3 -m pip install --user pipx\n\npipx install scml-vis\n```\n\n## Usage\n\nThe visualizer can be run using any of the following commands:\n```bash\nscmlv\nscmlvis\nscml-vis\n```\nHereafter we will use the shorter version.\n\n- To visualize any of the recently run worlds and tournaments just run:\n\t```bash\n\tscmlv show\n\t```\n\tThis will open your browser and allow you to choose a world or a tournament to\n\tdisplay.\n\t![show without parameters](docs/show.png)\n\n\t- If this is the first time you visualize logs in this folder, you will be asked\n\t  to compile visualization data\n\t\t![compile visualization data](docs/compile.png)\n\t- If visualization data is available (or your pressed the `compile visualization data` button), you can now start visualizing the logs\n\t\t![compile visualization data](docs/aftercompile.png)\n- To visualize the logs in a specific folder, you can directly pass the folder as in:\n  ```bash\n\tscmlv show -f path-to-your-folder\n\t```\n- It is also possible to just compile visualization data without running the visualizer using:\n  ```bash\n\tscmlv compile path-to-your-folder\n\t```\n- The visualizer creates a database that it uses to create all the figures you see. You can directly explore this database using:\n  ```bash\n\tscmlv explore path-to-your-folder\n\t```\n\tThis will open a [datasette](https://docs.datasette.io/en/stable/getting_started.html) page allowing you to explore this database\n\t![datasette](docs/datasette.png)\n\tThis dataset will contain 8 tables describing everything that was logged in the world or tournament. \n\t![datasette](docs/datasettelarge.png)\n\tPlease consult [datasette documentation](https://docs.datasette.io/en/stable/getting_started.html) for all the ways you can interact with this dataset.\n\n## Available visualizations\n\nTo visualize your logs, you need to follow three steps:\n\n1. Filter the dataset using the `Data Selection` section of the sidebar.\n2. Choose the **family** of figures you would like to show from the `Figure Selection` dropdown in the sidebar. Currently we provide `Time-series`, `Tables` and `others` that are always available as well as `Networks`  that are only available when you visualize a single world or filter the tournament to focus on a single world.\n3. Choose the specific graph you want to see from the family selected in the previous step.\n\nYou can watch [a demo of this process here](https://youtu.be/BCDjnnSmIsk)\n\n## TODO List (Good Ideas for PRs)\n\n- ~~Show negotiation logs (i.e. negotiation results)~~\n- ~~Display all contracts (i.e. in a table) based on selection criteria~~\n- ~~Zoom on negotiation details (i.e. exchanged offers)~~\n- ~~Add dynamic figures using plotly/altair~~\n- ~~Add networkx like graphs of contracts / negotiations / offers~~\n- ~~Allow starting the app without specifying a folder.~~\n- ~~Add new figure types that do not have time/step in the x-axis.~~\n- ~~Correcting the placement of weights on edges in network views.~~\n- Adding a graph showing negotiation history in the ufun-space of negotiators (will require a change in the scml package).\n- Add saving and loading of the visualizer\'s state (i.e. what is visible).\n- Resolving the strange behavior of CI bands in plotly in some cases.\n',
    'author': 'Yasser Mohammad',
    'author_email': 'yasserfarouk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/scml-vis/scml-vis',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
