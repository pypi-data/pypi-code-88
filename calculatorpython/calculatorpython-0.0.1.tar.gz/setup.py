from setuptools import setup, find_packages
VERSION = '0.0.1'
DESCRIPTION = 'Simple calculator'
LONG_DESCRIPTION = 'See README.md.'

# Setting up
setup(
    name="calculatorpython",
    version=VERSION,
    author="Advait Shiralkar",
    author_email="advaitshiralkar2@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['Calculator'],
    keywords=[''],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
