from setuptools import setup
import pathlib
from von import __version__, __author__


# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()


# Setting up
setup(
    name="von",
    version=__version__,
    description="test pip package",
    long_description=README,
    author=__author__,
    author_email="<vozon.537@gmail.com>",
    long_description_content_type="text/markdown",
    packages=["von"],
    license="MIT",
    url="https://github.com/nagendra-2k3/von",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "von = von:cmd",
        ],
    },
)
