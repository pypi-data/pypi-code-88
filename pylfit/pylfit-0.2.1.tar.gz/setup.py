import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylfit",
    version="0.2.1",
    author="Tony Ribeiro",
    author_email="tonyribeiro.research.aca@gmail.com",
    description="LFIT algorithms package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tony-sama/pylfit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
