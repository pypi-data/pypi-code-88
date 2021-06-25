"""iParcelBoxPy setup script."""
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="iParcelBoxPy",
    version="0.0.1",
    author="iParcelBox Ltd",
    author_email="support@iparcelbox.com",
    packages=["iparcelboxpy"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["requests"],
    url="https://github.com/gadget-man/iparcelboxpy",
    project_urls={
        "Bug Tracker": "https://github.com/gadget-man/iparcelboxpy/issues",
    },
    # download_url="https://github.com/gadget-man/iparcelboxpy/-/archive/master/....",
    license="MIT",
    description="Python wrapper for the iParcelBox Local API",
    platforms="Cross Platform",
)
