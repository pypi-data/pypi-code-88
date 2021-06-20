from setuptools import setup

url = "https://github.com/jic-dtool/dtool-tag"
version = "0.1.1"
readme = open('README.rst').read()

setup(
    name="dtool-tag",
    packages=["dtool_tag"],
    version=version,
    description="Add ability to tag datasets using the dtool CLI",
    long_description=readme,
    include_package_data=True,
    author="Tjelvar Olsson",
    author_email="tjelvar.olsson@gmail.com",
    url=url,
    install_requires=[
        "click",
        "dtoolcore>=3.17.0",
        "dtool-cli",
    ],
    entry_points={
        "dtool.cli": [
            "tag=dtool_tag.cli:tag",
        ],
    },
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
