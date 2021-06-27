import codecs
import os

from setuptools import find_packages, setup


def open_local(path, mode="r", encoding="utf8"):
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path)
    return codecs.open(path, mode, encoding)


long_description = ""
with open_local("README.md") as fp:
    long_description += fp.read()
    long_description += "\n"


setup(
    name="oop-event-bus",
    url="https://github.com/ChubV/oop-event-bus/",
    license="MIT",
    description="A simple OOP event bus",
    author="Vladimir Chub",
    author_email="v@chub.com.ua",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="utils",
    python_requires=">=3.9",
    packages=find_packages(exclude=("tests",)),
    install_requires=None,
    include_package_data=True,
    tests_require=["pytest", "pytest-asyncio"],
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
