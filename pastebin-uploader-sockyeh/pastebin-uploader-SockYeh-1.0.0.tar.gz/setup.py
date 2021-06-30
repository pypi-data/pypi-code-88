import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pastebin-uploader-SockYeh",
    version="1.0.0",
    author="SockYeh",
    author_email="author@example.com",
    description="This is a pastebin uploader with alot of features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SockYeh/Pastebin-Uplaoder",
    project_urls={
        "Bug Tracker": "https://github.com/SockYeh/Pastebin-Uplaoder/issues",
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