from setuptools import setup

setup(
    author="David Navarro Alvarez",
    author_email="me@davengeo.com",
    description="devops processor interface",
    url="https://github.com/davengeo/devopsprocessor-ifn",
    name="devopsprocessor-ifn",
    version='0.1.0',
    packages=[
        'devopsprocessor'
    ],
    install_requires=[
        'cloudevents'
    ],
    package_data={

    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Systems Administration',
    ]
)
