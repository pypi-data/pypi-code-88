import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lysis_curve",  # Package name
    version="1.0",
    author="Jake Chamblee",
    author_email='jchamblee1995@gmail.com',
    description="Lysis curve package",
    url='https://github.com/jakechamblee/Lysis-curve-plot',
    long_description=long_description,  # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['bacteriophage', 'phage', 'growth curve', 'lysis', 'graphing'],
    python_requires='>=3.6',
    py_modules=["lysis_curve"],  # Name of the python package
    package_dir={'': 'C:\\Users\jcham\PycharmProjects\lysis_curve_final'},
    install_requires=[]  # Install other dependencies if any
)
