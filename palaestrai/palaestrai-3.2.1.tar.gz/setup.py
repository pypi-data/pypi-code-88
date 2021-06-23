#!/usr/bin/env python3
"""Setup file for the ARL package."""
from setuptools import find_packages, setup


with open("VERSION") as freader:
    VERSION = freader.readline().strip()

with open("README.rst") as freader:
    README = freader.read()

install_requirements = [
    # CLI
    "click==7.1.2",
    "appdirs==1.4.4",
    # YAML
    "ruamel.yaml==0.17.4",
    # Process and IPC handling
    "aiomultiprocess==0.9.0",
    "setproctitle==1.2.2",
    "pyzmq==22.0.3",
    # Data handling and storage
    "alembic==1.5.8",
    "numpy==1.18.5",
    "pandas==1.2.4",
    "psycopg2-binary==2.8.6",
    "jsonpickle==2.0.0",
    "SQLalchemy < 1.4.0",
    "sqlalchemy_utils",
]

development_requirements = [
    # Tests
    "tox==3.23.0",
    "robotframework >= 4.0.0",
    "pytest==6.2.4",
    "pytest-asyncio",
    "pytest-cov",
    "coverage",
    "mypy",
    "black",
    "lxml",
]

extras = {"dev": development_requirements}

setup(
    name="palaestrai",
    version=VERSION,
    description="A Training Ground for Autonomous Agents",
    long_description=README,
    author="The ARL Developers",
    author_email="eric.veith@offis.de",
    python_requires=">=3.8.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=install_requirements,
    extras_require=extras,
    license="LGPLv2",
    url="http://palaestr.ai/",
    entry_points="""
        [console_scripts]
        palaestrai=palaestrai.cli.manager:cli
        arl-apply-migrations=palaestrai.store.migrations.apply:main
    """,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: "
        "GNU Lesser General Public License v2 (LGPLv2)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
