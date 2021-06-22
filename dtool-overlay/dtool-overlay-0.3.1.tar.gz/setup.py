from setuptools import setup

url = "https://github.com/jic-dtool/dtool-overlay"
version = "0.3.1"
readme = open('README.rst').read()

setup(
    name="dtool-overlay",
    packages=["dtool_overlay"],
    version=version,
    description="dtool CLI utilities for working with per item metadata",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@gmail.com",
    url=url,
    install_requires=[
        "dtoolcore",
        "parse",
        "click",
        "dtool-cli",
    ],
    entry_points={
        "dtool.cli": [
            "overlays=dtool_overlay.cli:overlays",
        ],
    },
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
