import setuptools
from setuptools import setup

with open("README.rst", "r", encoding="utf-8") as fh:
    ld = fh.read()


setup(
    name = "housing_price_pred",
    version = "0.0.1",
    author = "Sibashis Chakraborty",
    author_email = "sibashis.chakrab@tigeranalytics.com",
    url= "https://github.com/sibashisc/mle-training/tree/fix/9/ml-workflow",
    description = "Housing Price Prediction",
    long_description = ld,
    long_description_content_type = "text/markdown",
    py_modules = ["logger","ingest_data","train","score"],
    package_dir = {"": "src"},
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)