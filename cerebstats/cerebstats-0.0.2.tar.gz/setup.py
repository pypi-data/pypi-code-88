# ~/cerebstats/setup.py
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name="cerebstats",
        version="0.0.2",
        author="Lungsi",
        author_email="lungsi.sharma@unic.cnrs-gif.fr",
        #packages=find_packages(),
        packages=["cerebstats",
                  "cerebstats.data_conditions",
                  "cerebstats.stat_scores",
                  "cerebstats.hypothesis_testings"
                  ],
        url="https://github.com/cerebunit/cerebstats",
        download_url = "https://github.com/cerebunit/cerebstats/archive/refs/tags/v0.0.2.tar.gz",
        keywords = ["VALIDATION", "CEREBELLUM", "NEUROSCIENCE",
                    "MODELING", "SCIENTIFIC METHOD"],
        license="BSD Clause-3",
        description="Installable package 'cerebstats' for cerebunit",
        long_description="Statistical package necessary for running validation test on cerebellum models. Four components of CerebUnit: CerebModels, CerebData, CerebStats (install), and CerebTests (install).",
        install_requires=[
            "sciunit",
            "quantities",
            "scipy",
            "numpy",
            ],
        classifiers = [
            # "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as current state of package
            "Development Status :: 3 - Alpha",
            # Define audience
            "Intended Audience :: Developers",
            # License
            "License :: OSI Approved :: BSD License",
            # Specify supported python versions
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            ],
)
