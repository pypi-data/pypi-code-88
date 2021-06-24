from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.8'
DESCRIPTION = 'API-Wrapper WhatIsMyMMR'
LONG_DESCRIPTION = '''

Simple-Async API Wrapper for WhatIsMyMMR Website (League of Legends)

Creator-Attribution:

Title: WhatIsMyMMR

Creator: Josh Kross / josh@whatismymmr.com

Source: https://euw.whatismymmr.com/ / https://dev.whatismymmr.com/

License: https://creativecommons.org/licenses/by/4.0/


Disclaimer:


Use a unique and descriptive user agent string, which should include the target platform, a unique application identifier, and a version string.
The following format is recommended: <platform>:<app ID>:<version string>. For example, iOS:com.example.helloworld:v1.0.3.
Don’t lie about your user agent, such as spoofing popular browsers. This is a bannable offense.


Limit the rate of requests to 60 per minute.
The database server is only so powerful. If you think you’ll need a higher request rate, contact Josh before hitting the servers.


! All API Rights Reserved by the Owner of https://euw.whatismymmr.com - Josh !


'''

# Setting up
setup(
    name="mmrwrapper",
    version=VERSION,
    author="Sunta",
    author_email="noneofyour@business.com",
    license_files = ('LICENSE.txt',),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['asyncio', 'aiohttp'],
    keywords=['python', 'api', 'wrapper'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)