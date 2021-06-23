import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filabase",  # Replace with your own username
    version="0.1.0",
    author="Nikola Geneshki",
    author_email="ngeneshki@gmail.com",
    description='''A small package that provides utilities for using files as
    different types of databases''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/geneshki/filabase",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
