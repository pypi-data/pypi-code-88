# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hypercat']

package_data = \
{'': ['*']}

install_requires = \
['astropy',
 'h5py==2.9.0',
 'ipython>=7.24.1,<8.0.0',
 'jupyterlab>=3.0.16,<4.0.0',
 'matplotlib',
 'numpy',
 'pandas>=1.2.4,<2.0.0',
 'scikit-image',
 'scipy',
 'urwid>=2.0.1']

entry_points = \
{'console_scripts': ['hypercatgui = hypercatgui:main']}

setup_kwargs = {
    'name': 'hypercat',
    'version': '0.1.5',
    'description': 'Hypercube of clumpy AGN tori',
    'long_description': 'HYPERCAT\n========\n\nHypercubes of (clumpy) AGN tori\n\nSynopsis\n--------\n\nHandle a hypercube of CLUMPY brightness maps and 2D projected dust\nmaps. Easy-to-use classes and functions are provided to interpolate\nimages in many dimensions (spanned by the model parameters), extract\nmonochromatic or multi-wavelength images, as well as rotate images,\nzoom in and out, apply PSFs, extract interferometric signals, quantify\nmorphologies, etc.\n\nAuthors\n-------\n\nRobert Nikutta [\\<robert.nikutta@gmail.com\\>](mailto:robert.nikutta@gmail.com), Enrique Lopez-Rodriguez, Kohei Ichikawa\n\nVersion\n-------\n\nVersion fo this document: 2021-06-27\n\nCurrent version of the hypercat sofware: 0.1.5\n\nLicense and Attribution\n-----------------------\n\nHYPERCAT is open-source software and freely available at\nhttps://github.com/rnikutta/hypercat/ and\nhttps://pypi.org/project/hypercat/ under a permissive [BSD 3-clause\nlicense](./LICENSE)\n\nIn short, if you are using in your research any of the HYPERCAT\nsoftware or its components, and/or the HYPERCAT model data hypercubes,\nand/or telescope pupil images, please cite these two papers:\n\n- *Nikutta, Lopez-Rodriguez, Ichikawa, Levenson, Packham, Hönig,\n  Alonso-Herrero, "Hypercubes of AGN Tori (Hypercat) -- I. Models and\n  Image Morphology", ApJ (2021, accepted)*\n\n- *Nikutta, Lopez-Rodriguez, Ichikawa, Levenson, Packham, Hönig,\n  Alonso-Herrero, "Hypercubes of AGN Tori (Hypercat) -- II. Resolving\n  the torus with Extremely Large Telescopes", ApJ (2021, under\n  review)*\n\n\nMinimal install instructions\n----------------------------\n\nIf you don\'t mind installing HYPERCAT and its dependencies into your\ncurrent environment (real or virtual), simply run:\n\n```\npip install hypercat\n```\n\n\nIf you prefer to install HYPERCAT into a fresh new environment without affecting your existing Python installation, you can create a new environment in various ways.\n\n- If you are a user of conda / anaconda / miniconda / astroconda:\n\n```\nconda create -n hypercat-env python=3.7.2\nconda activate hypercat-env\n\npip install hypercat\n```\n\n- If you are a user of pyenv:\n\n```\npyenv install 3.7.2\n. .venv/bin/activate\n\npip install hypercat\n```\n\nHYPERCAT / CLUMPY model images and 2D dust cloud maps\n-----------------------------------------------------\n\nHypercat needs to access the hypercubes of Clumpy images and dust\nmaps. They can be downloaded as hdf5 files from the link given at\nhttps://www.clumpy.org/images/ (which currently is\nftp://ftp.noao.edu/pub/nikutta/hypercat/).\n\nThe software, and the example Jupyter notebooks (see below) will need\nto be instructed about the location of the model file(s). The is very\neasy to do upon loading the model file; the notebooks have several\nexamples on how to accomplish this, e.g.\n\n```\nimport hypercat as hc\nfname = \'hypercat_20181031_all.hdf5\' # use your local location to the HDF5 model file\ncube = hc.ModelCube(fname,hypercube=\'imgdata\')  # use \'imgdata\' for brightness maps, and \'clddata\' for 2D cloud maps\n```\n\nExample Jupyter notebooks\n-------------------------\n\nSeveral Jupyter example notebooks demonstrate some of HYPERCAT\'s functionality:\n\n- [01-hypercat-basics.ipynb](https://github.com/rnikutta/hypercat/tree/master/examples/01-hypercat-basics.ipynb):\n  Loading a model hypercube, generating model images, images at\n  multiple wavelengths, images at multiple values of other model\n  parameters, accessing cloud maps\n\n- [02-hypercat-astro.ipynb](https://github.com/rnikutta/hypercat/tree/master/examples/02-hypercat-astro.ipynb):\n  Adding physical units to images, world coordinate system, field of\n  view and pixel scale operations, image rotation / position angle,\n  saving to FITS files\n\n- [03-hypercat-singledish.ipynb](https://github.com/rnikutta/hypercat/tree/master/examples/03-hypercat-singledish.ipynb):\n  Telescope pupil images (JWST, Keck, GMT, TMT, ELT), simulating\n  observations with single-dish telescopes, noisy observations,\n  Richardson-Lucy deconvolotuion, detector pixel scale, flux\n  preservation, observations at multiple wavelengths\n\n- [04-hypercat-morphology-intro.ipynb](https://github.com/rnikutta/hypercat/tree/master/examples/05-hypercat-morphology-intro.ipynb):\n  Introduction to morphological measurements (on 2D Gaussians), image\n  centroid, rotation, measuring size of emission features, elongation,\n  half-light radius, Gini coefficient\n\n- [05-hypercat-morphology-clumpy.ipynb](https://github.com/rnikutta/hypercat/tree/master/examples/05-hypercat-morphology-clumpy.ipynb):\n  Morphology of the HYPERCAT model images; morphological sizes,\n  elongation, centroid location; compare morphologies of of emission\n  and their underlying dust distributions; from 2D cloud maps to real\n  cloud numbers per LOS; photon escape probability along a LOS\n\n\nUser Manual\n-----------\n\nFor more detailed installation instructions and other usage examples,\nplease see the HYPERCAT User Manual [User Manual](./docs/manual/) (in\naddition to the [example Jupyter notebooks](./examples/) )\n',
    'author': 'Robert Nikutta',
    'author_email': 'robert.nikutta@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rnikutta/hypercat',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.2',
}


setup(**setup_kwargs)
