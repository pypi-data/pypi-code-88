from setuptools import setup
__project__ = "get_chefkoch"
__version__ = "1.0.1"
__description__ = "Python library to interact with Chefkoch."

with open("README.md", "r") as fh:
    long_description = fh.read()

__packages__ = ["get_chefkoch"]
__keywords__ = ["Chefkoch","get_chefkoch"]
__requires__ = ["requests","feedparser","beautifulsoup4"]

setup(
    name = __project__,
    version = __version__,
    author = "olzeug",
    description = __description__,
    packages = __packages__,
    keywords = __keywords__,
    requires = __requires__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olzeug/get_chefkoch",
    python_requires='>=3.0',
)
