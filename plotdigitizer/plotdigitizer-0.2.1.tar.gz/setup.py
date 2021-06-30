# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['plotdigitizer']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0',
 'matplotlib>=3.3.4,<4.0.0',
 'numpy>=1.19.5,<2.0.0',
 'opencv-python>=4.5.1,<5.0.0']

entry_points = \
{'console_scripts': ['plotdigitizer = plotdigitizer.plotdigitizer:main',
                     'plotdigitizer-locate = plotdigitizer.locate:main']}

setup_kwargs = {
    'name': 'plotdigitizer',
    'version': '0.2.1',
    'description': 'Extract raw data from plots images',
    'long_description': "![Python application](https://github.com/dilawar/PlotDigitizer/workflows/Python%20application/badge.svg) [![PyPI version](https://badge.fury.io/py/plotdigitizer.svg)](https://badge.fury.io/py/plotdigitizer) [![DOI](https://zenodo.org/badge/140683649.svg)](https://zenodo.org/badge/latestdoi/140683649)\n\nA Python3 command line utility to digitize plots\n\nThis utility is useful when you have a lot of similar plots that needs to be\ndigitized such as EEG, ECG recordings. See examples below.\n\nFeel free to contact me for commercial work that may require optimizing this\npipeline for your use case. Please send a sample plot.\n\nFor occasional use, have a look at\n[WebPlotDigitizer](https://automeris.io/WebPlotDigitizer/) by Ankit Rohatagi.\n\n## Installation\n\n```\n$ python3 -m pip install plotdigitizer\n$ plotdigitizer --help\n```\n\n## Preparing image\n\nCrop the image and leave only axis and trajectories. I use\n`gthumb` utility on Linux. You can also use imagemagick or gimp.\n\nFollowing image is from MacFadden and Koshland, PNAS 1990 after trimming. One\ncan also remove top and right axis.\n\n![Trimmed image](./figures/trimmed.png)\n\n__Run__\n\n```bash\nplotdigitizer ./figures/trimmed.png -p 0,0 -p 10,0 -p 0,1\n```\n\nWe need at least three points (`-p` option) to map axes onto the image.  In the example\nabove, these are `0,0` (where x-axis and y-axis intesect) , `20,0` (a point on\nx-axis) and `0,1` (a point on y-axis). To map these points on the image, you\nwill be asked to click on these points on the image. _Make sure to click in\nthe same order and click on the points as precisely as you could. Any error in\nthis step will propagate._ If you don't have `0,0` in your image, you have to provide\n4 points: 2 on x-axis and 2 on y-axis.\n\nThe data-points will be dumped to a csv file specified by __`--output\n/path/to/file.csv`__.\n\nIf `--plot output.png` is passed, a plot of the extracted data-points will be\nsaved to `output.png`. This requires `matplotlib`. Very useful when debugging/testing.\n\n![](./figures/traj.png)\n\nNotice the error near the right y-axis.\n\n## Using in batch mode\n\nYou can pass the coordinates of points in the image at the command prompt.\nThis allows to run in the batch mode without any need for the user to click on\nthe image.\n\n```bash\nplotdigitizer ./figures/trimmed.png -p 0,0 -p 20,0 -p 0,1 -l 22,295 -l 142,295 -l 22,215 --plot output.png\n```\n\n### How to find coordinates of axes points\n\nIn the example above, point `0,0` is mapped to coordinate `22,295` i.e., the\ndata point `0,0` is on the 22nd row and 295th column of the image (_assuming that bottom left\nof the image is first row, first column `(0,0)`_). I have included an utility\n`plotdigitizer-locate` (script `plotdigitizer/locate.py`) which you can use to\nfind the coordinates of points.\n\n\n```bash\n$ plotdigitizer-locate figures/trimmed.png\n```\n\nor, from the source,\n\n```bash\n$ python3 plotdigitizer/locate.py figures/trimmed.png\n```\n\nThis command opens the image in a simple window. You can click on a point and\nits coordinate will be written on the image itself. Note them down.\n\n![](./figures/trimmed_locate.png)\n\n\n# Examples\n\n\n### Base examples\n\n```bash\nplotdigitizer figures/graphs_1.png \\\n\t\t-p 1,0 -p 6,0 -p 0,3 \\\n\t\t-l 165,160 -l 599,160 -l 85,60 \\\n\t\t--plot figures/graphs_1.result.png \\\n\t\t--preprocess\n```\n\n![original](./figures/graphs_1.png)\n![reconstructed](./figures/graphs_1.result.png)\n\n### Light grids\n\n```\nplotdigitizer  figures/ECGImage.png \\\n\t\t-p 1,0 -p 5,0 -p 0,1 \\\n        -l 290,337 -l 1306,338 -l 106,83 \\\n\t\t--plot figures/ECGImage.result.png\n```\n\n![original](./figures/ECGImage.png)\n![reconstructed](./figures/ECGImage.result.png)\n\n### With grids\n\n```\nplotdigitizer  figures/graph_with_grid.png \\\n\t\t-p 200,0 -p 1000,0 -p 0,50 \\\n        -l 269,69 -l 1789,69 -l 82,542 \\\n\t\t--plot figures/graph_with_grid.result.png\n```\n\n![original](./figures/graph_with_grid.png)\n_Image credit: Yang yi, Wang_\n\n![reconstructed](./figures/graph_with_grid.result.png)\n\n__Note that legend was not removed in the original figure and it has screwed up\nthe detection below it.__\n\n# Limitations\n\nCurrently this script has following limitations:\n\n- Background must not be transparent. It might work with transparent background but\n  I've not tested it.\n- Only b/w images are supported for now. Color images will be converted to grayscale upon reading.\n- One image should have only one trajectory.\n\n## Need help\n\nOpen an issue and please attach the sample plot.\n\n## Related projects by others\n\n1.  [WebPlotDigitizer](https://automeris.io/WebPlotDigitizer/) by Ankit\nRohatagi is very versatile.\n\n\n## Notes\n\n- grapvhiz version 2.47.2 is broken for some xml files. See\n<https://forum.graphviz.org/t/assert-sz-2-in-convertsptoroute/689>. Please use a\ndifferent version.\n",
    'author': 'Dilawar Singh',
    'author_email': 'dilawar.s.rajput@gmail.com',
    'maintainer': 'Dilawar Singh',
    'maintainer_email': 'dilawar.s.rajput@gmail.com',
    'url': 'https://github.com/dilawar/PlotDigitizer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
