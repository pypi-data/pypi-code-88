from setuptools import setup, find_packages

version = __import__("horuz").__version__

setup(
    name='horuz',
    version=version,
    description='Save and query your recon data on ElasticSearch.',
    url="https://github.com/misalabs/horuz",
    author='Misa G.',
    author_email="hi@misalabs.com",
    maintainer='Misa G.',
    maintainer_email='hi@misalabs.com',
    license='MIT license',
    packages=find_packages(),
    download_url = 'https://github.com/misalabs/horuz/archive/refs/tags/{}.tar.gz'.format(version),
    keywords = ['recon', 'elasticsearch', 'fuzzing', 'hacking'],
    include_package_data=True,
    install_requires=[
        'click',
        'elasticsearch==7.5.1',
        'requests==2.23.0',
        'dpath==2.0.1',
        'rich==9.13.0',
    ],
    entry_points='''
        [console_scripts]
        hz=horuz.cli:cli
    ''',
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
