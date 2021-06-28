from setuptools import setup, find_packages

setup(
    name="metodebibliotek", # Replace with your own username
    version="0.1.0",
    maintainer="Susie Jentoft",
    maintainer_email="susiejentoft@ssb.no",
    description="SSBs library for method functions",
    long_description="This is a meta-package with a collection of R and python function useful for official statistics production.",
    url="https://github.com/statisticsnorway/metodebibliotek",
    packages = find_packages(include = ["metodebibliotek"]),
    install_requires=[
        'requires',
        'numpy',
        'pandas',
        'datetime'
    ],
    python_requires='>=3.6',
)