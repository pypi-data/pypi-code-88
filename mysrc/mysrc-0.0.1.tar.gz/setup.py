from setuptools import setup, find_packages
classifiers=[
    'License :: OSI Approved :: MIT License'
]

setup(
    name="mysrc",
    version="0.0.1",
    description="Doing some awesome calculations",
    long_description = "This is my long description",
    author="Me",
    keyword='',
    # packages=['our_name_for_the_package_to_be_called_or_imported'],
    packages=find_packages(),
    # If our package has a prerequisite package
    install_requires=[],
    classifiers = classifiers
)
