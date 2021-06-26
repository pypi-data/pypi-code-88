import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eptc",
    version="0.0.3",
    author="elerp",
    author_email="hb@elerp.net",
    description="elerp python tools collection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.elerp.net/eptc/",
    project_urls={
        "Bug Tracker": "https://www.elerp.net/eptc/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)