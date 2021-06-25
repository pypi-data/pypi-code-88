#!/usr/bin/env python
from setuptools import setup

from mp import version

setup(
    name="mpfshell2",
    version=version.FULL,
    description="A simple shell based file explorer for ESP8266 and WiPy "
    "Micropython devices.",
    author="Stefan Wendler, with extensions by Hans Maerki",
    author_email="sw@kaltpost.de, hans@maerki.com",
    url="https://github.com/hmaerki/mpfshell2",
    download_url=f"https://github.com/hmaerki/mpfshell2/archive/v{version.FULL}.zip",
    install_requires=[
        "wheel ~= 0.36",
        "pyserial ~= 3.5",
        "colorama ~= 0.3.6",
        "websocket_client ~= 0.56",
        "pyusb ~= 1.1.1",  # for firmware updates using pydfu.py
        "dataclasses ~= 0.8; python_version < '3.7'",
    ],
    packages=["mp", "mp.firmware"],
    package_data={"mp": ["firmware/*.dfu"]},
    keywords=["micropython", "shell", "file transfer", "development"],
    classifiers=[],
    entry_points={"console_scripts": [
        "mpfshell=mp.mpfshell:main",
        "pyboard=mp.micropythonshell:main",
        "pyboard_query=mp.pyboard_query:main",
        "pyboard_pydfu=mp.firmware.pydfu:main",
        "pyboard_update=mp.firmware.update:main",
    ]},
)
