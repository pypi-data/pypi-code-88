import codecs
from setuptools import setup


DAO_VERSION = "0.0.1"
DOWNLOAD_URL = ""


def read_file(filename):
    """
    Read a utf8 encoded text file and return its contents.
    """
    with codecs.open(filename, "r", "utf8") as f:
        return f.read()


setup(
    name="daoism",
    packages=["youdao"],
    version=DAO_VERSION,
    description="A simple wrapper around Youdao API(WIP)",
    long_description=read_file("README.md"),
    license="MIT",
    author="Hou",
    author_email="hhhoujue@gmail.com",
    url="",
    download_url=DOWNLOAD_URL,
    keywords=["ocr", "translate", "dictionary", "youdao"],
    install_requires=["httpx"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Natural Language :: English",
    ],
    python_requires=">=3.7",
)
