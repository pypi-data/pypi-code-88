from setuptools import setup
from os import path
import glob

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="seiran",
    version="1.6.0",
    description="Local bookmarks manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet",
    ],
    keywords="bookmarks",
    url="https://www.twinkle-night.net/Code/seiran.html",
    author="Garrick",
    author_email="earthisthering@posteo.de",
    license="GPLv3+",
    packages=["seiran"],
    data_files=[
        ("seiran/docsource", glob.glob("docsource/*.*")),
        ("seiran/docsource/_static", glob.glob("docsource/_static/*")),
        ("seiran/docs", glob.glob("docs/html/*.*")),
        ("seiran/docs/_sources", glob.glob("docs/html/_sources/*")),
        ("seiran/docs/_static", glob.glob("docs/html/_static/*")),
    ],
    install_requires=["appdirs"],
    extras_require={
        "docs": ["sphinx>=3.4.1", "numpydoc"],
    },
    entry_points={"console_scripts": ["seiran=seiran.seiran:main"]},
    include_package_data=True,
    zip_safe=False,
)
