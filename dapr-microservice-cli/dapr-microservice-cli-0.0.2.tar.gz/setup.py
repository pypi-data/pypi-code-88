import setuptools

# Read package long description
with open('README.md', 'r') as h:
    long_description = h.read()

# Package setup
setuptools.setup(
    name='dapr-microservice-cli',
    version='0.0.2',
    author='li1234yun',
    author_email='li1234yun@163.com',
    description='dapr microservice cli',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['dapr_microservice_cli'],
    package_dir={'dapr_microservice_cli': 'dapr_microservice_cli'},
    include_package_data=True,
    # package_data={'dapr_microservice_cli': ['templates/*', 'templates/.gitignore']},
    # exclude_package_data={"": [".venv", ".env"]},
    install_requires=[
        'click >= "7.0.0"'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'dapr-microservice-cli = dapr_microservice_cli.run:cli'
        ]
    },
    python_requires=">=3.6"
)
