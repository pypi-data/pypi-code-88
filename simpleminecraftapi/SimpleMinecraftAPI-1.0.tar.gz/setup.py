from setuptools import setup,find_packages


setup(
   name='SimpleMinecraftAPI',
   version='1.0',
   description='SimpleMinecraftAPI that return skin,body,head,cape,id',
   license="MIT",
   long_description=open('README.txt').read(),
   author='Zaid Ali',
   author_email='realarty69@gmail.com',
   keywords=['minecraft','api'],
    packages=['SimpleMinecraftAPI'],
    install_requires=["requests"],
    package_dir={'SimpleMinecraftAPI': 'SimpleMinecraftAPI'},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)