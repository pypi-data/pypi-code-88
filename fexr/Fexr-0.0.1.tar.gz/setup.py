import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fexr",
    version="0.0.1",
    author="Fexr",
    author_email="nidhin@getfexr.com",
    description="REST Client for Fexr",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fexrapis/pyfexr",
    project_urls={
        "Bug Tracker": "https://github.com/fexrapis/pyfexr/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "fexr"},
    packages=setuptools.find_packages(where="fexr"),
    python_requires=">=3.6",
)