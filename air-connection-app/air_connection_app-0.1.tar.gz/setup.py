from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="air_connection_app",
    version="0.1",
    author="vverholyak",
    description="air connection app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab-1914910442.us-west-2.elb.amazonaws.com/vverkholyak/python_app",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[        
        'flask==1.1.2',
        'flask_restful==0.3.9',
        'flask_sqlalchemy==2.5.1',
        'mysql-connector-python==8.0.25',
        'marshmallow==3.12.1',
        'SQLAlchemy==1.4.15'
    ]
)
