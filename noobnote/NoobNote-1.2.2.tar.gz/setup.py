import setuptools 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NoobNote",
    version="1.2.2",
    description="A Simple Notepad",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://newtoallofthis123.github.io/NoobNote",
    author="NoobScience",
    author_email="noobscience123@gmail.com",
    license="MIT",
    project_urls={
        "Author WebSite" : "https://newtoallofthis123.github.io/About",
        "Bug Tracker": "https://github.com/newtoallofthis123/NoobNote/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=["PyQRCode", "pypng", "rich"],
    entry_points={
        "console_scripts": [
            "NoobNote=NoobNote.__main__:main",
        ]
    },
)