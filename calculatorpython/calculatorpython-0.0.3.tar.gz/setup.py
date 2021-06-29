from setuptools import setup, find_packages
VERSION = '0.0.3'
DESCRIPTION = 'Calculator with simple operations'
LONG_DESCRIPTION = 'Note: Argument one in every attribute in operated on with Argument one.'


# Setting up
setup(
    name="calculatorpython",
    version=VERSION,
    author="Advait Shiralkar",
    author_email="advaitshiralkar2@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description= LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['Calculator'],
    keywords=[''],
    License='MIT',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
