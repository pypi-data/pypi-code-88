import setuptools
from setuptools import version


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="leolib",
    version="1.0.4",
    author="AntonVanke",
    author_email="fjs0801@gmail.com",
    description="利昂图书馆api打包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        "requests"
    ],
    python_requires='>=3'

)
