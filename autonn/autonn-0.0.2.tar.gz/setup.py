import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.readlines()

__version__ = "0.0.2"

setuptools.setup(
    name="autonn",
    version=__version__,
    author="Hao Wang, Yuanhao Guo, and Zhiheng Li",
    description=(
        "Configurable deep neural networks for neural architecture search"
        "and hyper-parameter tuning; Cloud deployment of DNN models"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
