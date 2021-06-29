import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="pj_rf_sshdb",
    version="0.0.6",
    description="Get Data from DB via SSh during execution using Robot Framework..",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    author="PJ Gevana",
    author_email="patdroidz@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pj_rf_sshdb"],
    include_package_data=True,
    # install_requires=["requests"],
)
