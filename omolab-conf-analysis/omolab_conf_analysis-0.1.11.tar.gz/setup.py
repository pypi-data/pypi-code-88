from setuptools import setup
from codecs import open as copen
from os import path

here = path.abspath(path.dirname(__file__))

# with open("README.md", "r") as fh:
#     long_description = fh.read()


# Get the long description from the README file
with copen(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Get the dependencies and installs
with copen(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if x.startswith("git+")]

setup(
    name= "omolab_conf_analysis",
    version="0.1.11",
    description="Uses PCA and K-means clustering to separate conformational ensembles. (xyz-files only)",
    py_modules=["clustering","ConformationalAnalysis","pymol","xyz",
                "pca_creation","elements","mGenerate_conf_analysis","mGenerate_PyMOL_Session"],
    scripts=["mGenerate_conf_analysis.sh","mGenerate_PyMOL_Session.sh"],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: MacOS X",
        "Framework :: Matplotlib",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: Free For Educational Use",
        "License :: Free For Home Use",
        "License :: Free for non-commercial use",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Information Analysis"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires= install_requires,
    dependency_links= dependency_links,
    url = "https://github.com/mattnw1/Conformational_Analysis",
    author="Matthew Nwerem",
    author_email="nwere100@mail.chapman.edu"

)

#mGenerate_PyMOL_Session.sh cannot be included here because it is not a .py file, must find another way to add it
