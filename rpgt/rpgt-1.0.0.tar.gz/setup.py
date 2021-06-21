"""
The setup file for this package
"""
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpgt",
    version="1.0.0",
    description="Automated Repository and Pipeline Generation for Data-Science Projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/tweet.dimitri/rpgt",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "pipenv",
        "mllint",
        "isort",
        "pylint",
        "mypy",
        "bandit",
        "black",
        "dvc",
    ],
    entry_points={
        "console_scripts": [
            "rpgt=rpgt.src.__main__:main",
        ]
    },
)
