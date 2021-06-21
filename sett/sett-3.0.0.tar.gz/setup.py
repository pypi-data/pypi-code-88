#!/usr/bin/env python3

import os
import sys
from datetime import datetime
from setuptools import setup, find_packages

sys.path.insert(0, os.path.dirname(__file__))

# pylint: disable=wrong-import-position
from sett import URL_READTHEDOCS, URL_GITLAB

# 0.0.0-dev.* version identifiers for development only (not public)
__version__ = "0.0.0.dev" + datetime.now().strftime("%Y%m%d")

if __name__ == "__main__":
    setup(
        name="sett",
        version="3.0.0",
        license="LGPL3",
        description="Data compression, encryption and transfer tool",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        author="Robin Engler, "
        "Jarosław Surkont, "
        "Gerhard Bräunlich, "
        "Kevin Sayers, "
        "Christian Ribeaud, "
        "François Martin",
        author_email="robin.engler@sib.swiss, "
        "jaroslaw.surkont@unibas.ch, "
        "gerhard.braeunlich@id.ethz.ch, "
        "sayerskt@gmail.com, "
        "christian.ribeaud@karakun.com, "
        "francois.martin@karakun.com",
        url="https://gitlab.com/biomedit/sett",
        install_requires=[
            "PySide6>=6.1.0, !=6.1.1",
            "colorama>=0.4.4",
            "dataclasses ; python_version<'3.7'",
            "gpg-lite>=0.9.0, <0.10.0",
            "libbiomedit>=0.3.0, <0.4.0",
            "paramiko>=2.7.1",
            "typing_extensions ; python_version<'3.8'",
        ],
        extras_require={
            "socks": ["PySocks"],
            "legacy": ["PySide2>=5.15.1"],
            "benchmark": ["pandas", "matplotlib", "seaborn"],
        },
        packages=find_packages(exclude=["test", "test.*", "benchmark"]),
        package_data={"sett": ["py.typed"]},
        zip_safe=False,
        python_requires=">=3.6",
        entry_points={
            "console_scripts": ["sett=sett.cli:run"],
            "gui_scripts": ["sett-gui=sett.gui:run"],
        },
        test_suite="test",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
            "Operating System :: OS Independent",
        ],
        project_urls={
            "Documentation": URL_READTHEDOCS,
            "Source": URL_GITLAB,
        },
    )
