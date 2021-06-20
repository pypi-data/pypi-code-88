import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="byestore",
    version="0.0.4",
    author="ByeMC",
    author_email="byestore@byemc.xyz",
    description="A library for ByeStore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/byestore/byestorelibs",
    project_urls={
        "Bug Tracker": "https://github.com/byestore/byestorelibs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Internet :: WWW/HTTP",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)