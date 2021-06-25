from setuptools import find_packages, setup

pkgs = find_packages('.')

setup_kwds = dict(
    name="manpy",
    version="0.0.1",
    author="Florian Gacon",
    author_email="florian.gacon@gmail.com",
    package_dir={'':'.'},
    packages=pkgs,
    zip_safe=False,
    entry_points={'console_scripts': ['manpy=manpy._cli:main']}
)

setup(**setup_kwds)