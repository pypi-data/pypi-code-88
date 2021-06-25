# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alguns']

package_data = \
{'': ['*']}

install_requires = \
['cffi==1.14.5', 'cryptography==3.4.7', 'pycparser==2.20', 'six>=1.16.0,<2.0.0']

setup_kwargs = {
    'name': 'alguns',
    'version': '0.1.4',
    'description': 'A crypto library for encrypting text data.',
    'long_description': "# Alguns\n\nAlguns is a symmetric encryption method that contains 2 keys, without which decryption of the message is impossible.\n\nAlguns also uses 128-bit AES in CBC mode and PKCS7 padding. \n\nLetters and symbols are encrypted using the replacement method generate_replacement. A replacement character for a letter consists of [randomSymbol, randomNumber(0,99), randomSymbol, randomNumber(0,99)].\nA Alguns key as returned by the generate_key actually contains two 16-byte keys:\nA signing key used to sign the HMAC.\n\nA private key used by the encryption.\nThese two values are concatenated to form a 32 byte value. This 32 byte key is then encoded using Base64 encoding. This encodes the binary quantity as string of ASCII characters. The variant of Base64 used is URL and filename safe, meaning that it doesn't contain any characters that aren't permitted in a URL or a valid filename in any major operating system.\n\n-------------------------\n\n### Supported Languages:\n- Russian\n- English\n\n-------------------------\n\n### Installation\n\n###### The installation method for this module is shown below.\n\n`pip3 install alguns`\n\n-------------------------\n\n###### How generate keys?\n```python\nkey = Alguns.generate_key()\nreplacement = Alguns.generate_replacement()\n# Put this somewhere safe!\n```\n\n###### How to encrypt a message?\n\n```python\nmykey = # My key that I created earlier.\nmyreplacement = # My replacement that I created earlier.\nal = Alguns(key=mykey, replacement=myreplacement)\nmsgcrypt = al.encrypt('Hellow it is my message! Привет, это мое сообщение...')\nprint(msgcrypt)\n# gAAAAABewxb_nE1mbHgN7ma79_XAbh68hLblIFdX3czIEmUDCSFWxMXTTEdIU5...\n```\n\n###### How to decrypt a message?\n\n```python\nal = Alguns(key=mykey, replacement=myreplacement)\nmsgdecrypt = al.decrypt('gAAAAABewxb_nE1mbHgN7ma79_XAbh68hLblIFdX3czIEmUDCSFWxMXTTEdIU5...')\nprint(msgdecrypt)\n# Hellow it's my message! Привет, это мое сообщение...",
    'author': 'dotX12',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dotX12/AlgunsCrypt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
}


setup(**setup_kwargs)
