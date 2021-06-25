from setuptools import setup, find_packages
#import npsdk

with open("README.md", mode="r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name='npsdk',
    description="Nezip Python SDK",
    version='0.9.1',
    author='xxg',
    author_email='752299578@qq.com',
    url='https://www.npsdk.com', 
    long_description=long_description,
    long_description_content_type="text/markdown",
    #packages=setuptools.find_packages(include=['npsdk', 'npsdkapi.py', 'npdatapoolthread.py', 'npsdkobjs.py', 'Stockdrv.py']),
    packages=find_packages(),
    license='Apache License 2.0',
    classifiers=[
        'Natural Language :: English',
        "License :: OSI Approved :: Apache Software License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Communications', 'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking'
    ],
    zip_safe=True,
    python_requires='>=3.6',
    install_requires=["websocket-client>=1.0.1", "numpy", "pandas"],

    
)