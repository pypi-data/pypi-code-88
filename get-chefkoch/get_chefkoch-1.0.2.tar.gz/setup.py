from setuptools import setup
__project__ = "get_chefkoch"
__version__ = "1.0.2"
__description__ = "Python library to interact with Chefkoch."

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = __project__,
    version = __version__,
    author = "olzeug",
    description = __description__,
    license = 'MIT',
    packages = ["get_chefkoch"],
    keywords = ["Chefkoch","get_chefkoch"],
    install_requires = ["requests","feedparser","beautifulsoup4"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olzeug/get_chefkoch",
    python_requires='>=3.0',
)
