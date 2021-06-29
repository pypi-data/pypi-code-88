import re

import setuptools

with open("GODBOY/version.py", "rt", encoding="utf8") as x:
    version = re.search(r'__version__ = "(.*?)"', x.read()).group(1)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

name = "GODBOY"
author = "GODBOYX"
author_email = "rj05tilak@gmail.com"
description = "A Secure  and Powerful Python-Telethon Based Library For Userbots."
license = "GNU AFFERO GENERAL PUBLIC LICENSE (v3)"
url = "https://github.com/GODBOYX/GODBOY"

setuptools.setup(
    name=name,
    version=version,
    author=author,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    license=license,
    packages=setuptools.find_packages(),
    install_requires=[
        "telethon",
        "python-decouple==3.3",
        "TgCrypto",
        "python-dotenv==0.15.0",
        "cloudscraper",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
