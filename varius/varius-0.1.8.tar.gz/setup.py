from setuptools import find_packages, setup

from varius import __version__

# load readme
with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="varius",
    version=__version__,
    author="Chenchao Zhao",
    author_email="chenchao.zhao@gmail.com",
    description="Perform calculation with various versions of variables",
    packages=find_packages(exclude=["tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["sympy", "dataclasses"],
    license="MIT",
)
