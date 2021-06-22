# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['uberlimb', 'uberlimb.model']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0',
 'Wand>=0.6.6,<0.7.0',
 'coverage>=5.5,<6.0',
 'ffmpeg-python>=0.2.0,<0.3.0',
 'numpy>=1.19.5,<2.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'pytest>=6.2.4,<7.0.0',
 'scikit-image>=0.18.1,<0.19.0',
 'tensorflow>=2.5.0,<3.0.0']

setup_kwargs = {
    'name': 'uberlimb',
    'version': '0.4.1',
    'description': 'Generative art with CPPN networks.',
    'long_description': '# ÜberLimb\n\nGenerative art with CPPN networks.\n\n# Get started\n\n```python\nfrom uberlimb.renderer import Renderer\nfrom uberlimb.parameters import RendererParams\n\nrenderer = Renderer(RendererParams())\nrenderer.render_frame().as_pillow().show()\n```\n\nExpected output:\n\n![](https://cai-misc.s3.eu-central-1.amazonaws.com/uberlimb/uberlimb_splash.png)\n\n# TODO\n- [ ] video pipeline\n- [ ] color schemes, both predefined and custom (will require varying\n  the number of output channels)',
    'author': 'Vladimir Sotnikov',
    'author_email': 'vladimir.sotnikov@jetbrains.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://cai.jetbrains.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
