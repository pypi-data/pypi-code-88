import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "f99_erp_api",                     # This is the name of the package
    version = "1.0.18",                        # The initial release version
    author = "DTQ",                     # Full name of the author
    description = "F99 Erp API",
    long_description = long_description,      # Long description read from the the readme file
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),    # List of all python modules to be installed
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires = '>=3.6',                # Minimum version requirement of the package
    py_modules = ["f99_erp_api_pb2", "f99_erp_api_pb2_grpc"],             # Name of the python package
    package_dir = {'':'.'},     # Directory of the source code of the package
    install_requires = ["grpcio==1.26.0", "grpcio-tools==1.26.0"]                     # Install other dependencies if any
)