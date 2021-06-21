from setuptools import setup

setup(name = 'idsl_gauge',
    author = 'Josef Matondang',
    author_email = 'admin@josefmtd.com',
    version = '1.0.0',
    description = 'Unofficial Python Wrapper for IDSL Tide Gauge API',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords = 'tsunami',
    url = 'https://github.com/josefmtd/idsl-gauge',
    license = 'MIT',
    packages = ['idsl_gauge'],
    install_requires = [
        'pandas'
    ],
    include_package_data = True,
    zip_safe = False)
