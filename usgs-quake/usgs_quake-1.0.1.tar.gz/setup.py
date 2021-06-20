from setuptools import setup

setup(name = 'usgs_quake',
    author = 'Josef Matondang',
    author_email = 'admin@josefmtd.com',
    version = '1.0.1',
    description = 'USGS Earthquake Real-time Feed and Historical Data',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords = 'earthquake',
    url = 'https://github.com/josefmtd/usgs-quake',
    license = 'MIT',
    packages = ['usgs_quake'],
    install_requires = [
        'pandas'
    ],
    include_package_data = True,
    zip_safe = False)
