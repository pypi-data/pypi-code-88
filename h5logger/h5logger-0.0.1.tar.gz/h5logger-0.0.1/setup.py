import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="h5logger",
    version="0.0.1",
    author="Randall Balestriero",
    author_email="randallbalestriero@gmail.com",
    description="h5 logger in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RandallBalestriero/h5logger",
    project_urls={
        "Bug Tracker": "https://github.com/RandallBalestriero/h5logger/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "h5logger"},
    packages=setuptools.find_packages(where="h5logger"),
    python_requires=">=3.6",
    install_requires=["h5py", "numpy"],
)
