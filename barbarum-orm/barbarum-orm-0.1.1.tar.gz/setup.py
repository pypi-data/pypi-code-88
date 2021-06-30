import setuptools

from barbarum_orm import project_name, project_version, author_name, author_email

with open("README.md", "r", encoding="utf-8") as stream: 
    long_description = stream.read()
with open("requirements.txt", "r", encoding="utf-8") as stream: 
        requirements = stream.read()
required_list = [item for item in requirements.split("\n") if item is not None and len(item.strip()) > 0]

setuptools.setup(
    name = project_name, 
    version = project_version, 
    author = author_name,
    author_email = author_email, 
    description = "Barbarum ORM framework",
    long_description = long_description, 
    url = "https://github.com/barbarum/barbarum-orm-python.git",
    packages = setuptools.find_packages(),
    include_package_data = True,
    package_data = {
        "": ["*.yaml"]
    }, 
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ], 
    install_requires = required_list, 
    python_requires = '>=3.5',
)