"""Setup file"""

import pathlib
from typing import List

from setuptools import find_packages, setup

from deepchain.version import VERSION

HERE = pathlib.Path(__file__).parent
LONG_DESC = (HERE / "LONG_DESC.md").read_text()


def read_requirements() -> List:
    with open("requirements.txt", "r+") as file:
        requirements = [line.strip() for line in file.readlines()]

    return requirements


def make_install():
    """main install function"""
    setup_fn = setup(
        name="deepchain-apps",
        license="Apache-2.0",
        version=VERSION,
        description="Define a personnal app to deploy on DeepChain.bio",
        author="Instadeep",
        long_description=LONG_DESC,
        long_description_content_type="text/markdown",
        author_email="a.delfosse@instadeep.com",
        packages=find_packages(exclude=["tests"]),
        entry_points={
            "console_scripts": ["deepchain=deepchain.cli.deepchain_cli:main"],
        },
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3.7",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
            "Topic :: Software Development",
        ],
        install_requires=read_requirements(),
        include_package_data=True,
        zip_safe=False,
        python_requires=">=3.7",
    )

    return setup_fn


if __name__ == "__main__":
    make_install()
