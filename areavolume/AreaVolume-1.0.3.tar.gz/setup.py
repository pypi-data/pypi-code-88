from setuptools import setup, find_packages

VERSION = '1.0.3' 
DESCRIPTION = 'AreaVolume Python package'
LONG_DESCRIPTION = 'has useful methods for area, volume computations'

setup(
       # the name must match the folder name 'AreaVolume'
        name="AreaVolume", 
        version=VERSION,
        author="Ausif Mahmood",
        author_email="ausif@xyz.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # specify any additional packages that 
        # need to be installed along with your package. Eg: 'numpy'
        
        keywords=['python', 'area', 'volume'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
