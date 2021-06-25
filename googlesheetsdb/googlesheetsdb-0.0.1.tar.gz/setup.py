from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'tools to use google sheets as a relational-ish database because why not'

# Setting up
setup(
    name="googlesheetsdb",
    version=VERSION,
    author="Blitz#6652",
    author_email="<blitz2k4.dev@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['google-api-python-client', 'google-auth-httplib2', 'google-auth-oauthlib'],
    keywords=['sheets', 'google sheets', 'google', 'database', 'db'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)