from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


setup(
    author="Altmirai LLC",
    author_email='kyle.stewart@altmirai.com',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],
    description="A command line tool that provides the functionality to use AWS CloudHSM services as a bitcoin wallet.",
    name='piggycli',
    version='0.0.20',
    packages=find_packages(),
    install_requires=['click', 'paramiko', 'scp', 'boto3',
                      'base58', 'ecdsa', 'requests', 'blockcypher'],
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'piggy=app.routes.click:piggy'
        ]
    },
    url='',
    keywords='altpiggybank'
)
