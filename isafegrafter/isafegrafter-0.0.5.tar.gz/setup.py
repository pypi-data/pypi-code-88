import setuptools

setuptools.setup(
    name="isafegrafter",
    version="0.0.5",
    author="ink",
    author_email="ink@isafetech.cn",
    description="Package for request forwarding.",
    long_description='Package for request forwarding..',
    long_description_content_type="text/markdown",
    url="https://github.com/inksong/isafegrafter",
    project_urls={
        "Bug Tracker": "https://github.com/inksong/isafegrafter/issues",
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