from setuptools import setup, find_packages

# python setup.py bdist_wheel sdist
# twine upload dist/*

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['click', 'pexpect']

setup(
    author="Altmirai LLC",
    author_email='kyle.stewart@altmirai.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Pexpect scripts to run on AWS EC2 to connect to CloudHSM Management Utility and CloudHSM",
    name='piggy-scripts',
    version='0.0.18',
    py_modules=['piggy-scripts'],
    packages=find_packages(exclude=[
        'docs',
        'tests',
    ]),
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points='''
        [console_scripts]
        script=app.routes.click:script''',
    url='',
    keywords='altpiggybank'
)
