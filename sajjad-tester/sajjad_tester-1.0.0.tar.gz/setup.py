from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="sajjad_tester",
    version="1.0.0",
    description="test description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="MSK",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License"
    ],
    keywords="sajjad testing something",
    packages=find_packages(),
    install_requires=["selenium>=3.141.0"],
    python_requires="~=3.5"
)
