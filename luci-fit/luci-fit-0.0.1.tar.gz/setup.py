from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'General Purpose Emission Line Fitting Package'
LONG_DESCRIPTION = 'General purpose emission line fitting package developed for the SITELLE IFU'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="luci-fit",
        version=VERSION,
        author="Carter Rhea",
        author_email="carter.rhea@umontreal.ca",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that
        # needs to be installed along with your package. Eg: 'caer'
        keywords=['python', 'luci-fit'],
        classifiers= [
            "Programming Language :: Python :: 3",
        ]
)
