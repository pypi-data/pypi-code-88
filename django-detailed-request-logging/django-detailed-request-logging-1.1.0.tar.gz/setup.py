#!/usr/bin/env python3

from datetime import datetime
from setuptools import setup, find_packages

# 0.0.0-dev.* version identifiers for development only (not public)
__version__ = "0.0.0.dev" + datetime.now().strftime("%Y%m%d")

setup(
    name="django-detailed-request-logging",
    version="1.1.0",
    license="LGPL3",
    description="Middleware to log requests in Django with more detailed information.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jaroslaw Surkont, "
    "Gerhard Bräunlich, "
    "Robin Engler, "
    "Christian Ribeaud, "
    "François Martin",
    author_email="jaroslaw.surkont@unibas.ch, "
    "gerhard.braeunlich@id.ethz.ch, "
    "robin.engler@sib.swiss, "
    "christian.ribeaud@karakun.com, "
    "francois.martin@karakun.com",
    url="https://git.dcc.sib.swiss/biwg/libweb/django-detailed-request-logging",
    python_requires=">=3.7",
    install_requires=["Django>=3.2", "djangorestframework>=3.12"],
    extras_require={
        "test": [
            "assertpy",
            "pytest",
            "pytest-django",
        ],
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    zip_safe=False,
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
)
