"""Basic install script."""

from setuptools import setup, find_packages  # type: ignore

setup(
    name="kep-solver",
    keywords="kidney kidney_exchange",
    packages=find_packages(exclude=["*test"]),
    install_requires=["defusedxml", "pulp"]
)
