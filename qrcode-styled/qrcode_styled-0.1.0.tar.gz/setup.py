# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qrcode_styled',
 'qrcode_styled.base',
 'qrcode_styled.pil',
 'qrcode_styled.pil.figures',
 'qrcode_styled.svg',
 'qrcode_styled.svg.figures']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0', 'qrcode>=6.1,<7.0']

extras_require = \
{'svg': ['lxml>=4.6.3,<5.0.0']}

setup_kwargs = {
    'name': 'qrcode-styled',
    'version': '0.1.0',
    'description': 'Python port for kozakdenys/qr-code-styling',
    'long_description': "# [WIP] QRCode Styled Generator\n\n### This is a python port for a [browser QRCode generator](https://github.com/kozakdenys/qr-code-styling) by [Denys Kozak](https://github.com/kozakdenys)\n\n```python\nfrom qrcode_styled import QRCodeStyled\n\nqr = QRCodeStyled()\n\n# Save to file\nwith open('test.webp', 'wb') as _fh:\n    qr.get_image('payload').save(_fh, 'WEBP', lossless=False, quaility=80, method=2)\n\n# Get to BytesIO buffer\nqrcode = qr.get('payload', _format='WEBP', lossless=False, quality=80, method=2)\n\n\n# Also supports basic asyncio workaround\nasync def main():\n    with open('test.webp', 'wb') as fh:\n        img = await qr.get_image_async('payload')\n        img.save(fh, 'WEBP', lossless=False, quaility=80, method=2)\n\n    qrcode = await qr.get_async('payload', _format='WEBP', lossless=False, quality=80, method=2)\n\n\n# You may put Image in the center of a QR Code\n\nfrom PIL import Image\n\nim = Image.open('image.png')\nqrcode = qr.get('payload', im, _format='WEBP')\n```\n\n![Example 1](./test.webp)",
    'author': 'Bogdan Parfenov',
    'author_email': 'adam.brian.bright@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://cifrazia.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
