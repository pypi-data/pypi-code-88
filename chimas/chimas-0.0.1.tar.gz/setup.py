import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chimas", # Replace with your own username
    version="0.0.1",
    author="chimas Staff",
    author_email="kassivs+chimas@gmail.com",
    description="Discussion Forum API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TryChimas/chimas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
