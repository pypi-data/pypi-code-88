from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['click']


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
    description="A command line tool that provides the functionality to use AWS CloudHSM services as a bitcoin wallet.",
    name='piggycli',
    version='0.0.7',
    py_modules=['piggycli'],
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points='''
        [console_scripts]
        piggy=piggycli.app.routes.click:piggy''',
    url='',
    keywords='altpiggybank'
)
