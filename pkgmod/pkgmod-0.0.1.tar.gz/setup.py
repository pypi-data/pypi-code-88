import io
import re
import setuptools

with io.open("README.md", "rt", encoding="utf8") as f:
    long_description = f.read()

with io.open("pkgmod/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"""__version__ = \"(.*?)\"""", f.read()).group(1)

requirements = ['isort']

setuptools.setup(
    author_email="nagy.attila@gmail.com",
    author="NAGY, Attila",
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Get module names from installed package names and back",
    install_requires=requirements,
    long_description_content_type="text/markdown",
    long_description=long_description,
    name="pkgmod",
    packages=setuptools.find_packages(),
    url="https://github.com/Mikata-Project/pkgmod",
    version=version,
)
