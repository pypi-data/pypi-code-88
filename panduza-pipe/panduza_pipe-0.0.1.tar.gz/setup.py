from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Wrapper for Panduza REST API Calls'
LONG_DESCRIPTION = 'This library provides simple wrapper to help implementing tests through panduza server'

# Setting up
setup(
        name="panduza_pipe", 
        version=VERSION,
        author="Panduza Team",
        author_email="panduza.team@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        
            
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            'Operating System :: POSIX',
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)


