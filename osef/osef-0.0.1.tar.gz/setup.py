"""To easily install project."""
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="osef",
    version="0.0.1",
    packages=["osef"],
    author="Adam Fourure",
    author_email="afo@outsight.tech",
    description="Osef file/stream tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["numpy==1.19.5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
