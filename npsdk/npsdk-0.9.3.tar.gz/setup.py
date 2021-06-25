from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel

with open("README.md", mode="r", encoding='utf-8') as fh:
    long_description = fh.read()
    
setup(
    name='npsdk',
    description="Nezip Python SDK",
    version='0.9.3',
    author='nfjd',
    author_email='752299578@qq.com',
    url='https://www.npsdk.com', 
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["npsdk"],
    package_data={'npsdk': ['npsdk.ini']}, 
    #packages=find_packages(),
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
    python_requires='>=3',
    install_requires=["websocket-client>=1.0.1", "numpy", "pandas", "psutil"],
    cmdclass={'bdist_wheel': bdist_wheel},

)