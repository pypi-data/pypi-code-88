import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="radgrafter",
    version="0.0.1",
    author="ink",
    author_email="ink@isafetech.cn",
    description="Package for request forwarding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inksong/radgrafter",
    project_urls={
        "Bug Tracker": "https://github.com/inksong/radgrafter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=2.7",
)