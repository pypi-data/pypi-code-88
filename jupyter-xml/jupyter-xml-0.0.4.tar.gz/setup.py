import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter-xml",
    version="0.0.4",
    author="Lars Pieschel",
    author_email="lars.pieschel@rwth-aachen.de",
    description="Jupyter Notebook Plugin for XML, XMLSchema and XPath support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.rwth-aachen.de/l.pieschel/jupyter-xml",
    packages=setuptools.find_packages(),
    install_requires=[
        "lxml>=4.6.2",
        "ipython>=7.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: IPython",
    ],
    python_requires='>=3.6',
)