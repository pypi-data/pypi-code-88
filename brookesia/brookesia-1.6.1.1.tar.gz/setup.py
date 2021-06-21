import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
name    = "brookesia",
    version = '1.6.1.1',
    author  = "Alexis Matynia",
    author_email = "alexis.matynia@sorbonne-universite.fr",
    description  = "Brookesia is a python-based program dedicated to the reduction ad the optimization of kinetic mechanisms.",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url          = "https://github.com/Brookesia-py/Brookesia",
    packages     = setuptools.find_packages(),
    classifiers  = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 
