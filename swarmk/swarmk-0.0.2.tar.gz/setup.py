from setuptools import setup ,find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()
    
setup(
    name='swarmk',
    version='0.0.2',
    description='pip install swarmk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/mohammed-Emad/particle-swarm-optimized-clustering',
    packages=['swarmk'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author='mlib_4_you',
    author_email='Atlantes0land@gmail.com',
    install_requires = [
        'numpy',
        'pandas',
    ],
    keywords=['swarm' ,'swarmk' ,'swarm lib' ,'pos' ,'swarm clustering', 'particle-swarm-optimized-clustering']
)
