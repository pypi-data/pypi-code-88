from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Busslina Library'
LONG_DESCRIPTION = 'Busslina Library'

# Setting up
setup(
    name="busslina-library",
    version=VERSION,
    author="Busslina (Vicente Bincaz)",
    author_email="<busslina@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'general', 'library'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
