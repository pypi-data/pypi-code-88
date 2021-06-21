import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py4hy",
    version="0.0.1",
    author="Matti Nelimarkka",
    author_email="matti.nelimarkka@helsinki.fi",
    description="Python libraries for University of Helsinki internal services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uh-soco/pyhy/",
    project_urls={
        "Bug Tracker": "https://github.com/uh-soco/pyhy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.5",
    install_requires = ['requests']
)
