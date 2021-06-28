import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()

setuptools.setup(
    name="Asthowen",
    version="0.0.0",
    author="Asthowen",
    description="The Python wrapper for the Asthowen API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Asthowen/AsthowenAPI",
    packages=setuptools.find_packages(),
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=[]
)
