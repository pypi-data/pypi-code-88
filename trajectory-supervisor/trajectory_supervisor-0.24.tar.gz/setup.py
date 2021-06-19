import setuptools

"""
NOTE: This script is only used for package generation! Do not execute, unless intended package changes.

1. Package can be built with following command:
python3 setup.py sdist bdist_wheel

2a. Package on pypi.org can be updated with the following command:
sudo python3 -m twine upload --skip-existing dist/*

2b. Install locally only:
python3 -m pip install dist/xxxxxxx.whl
"""

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='trajectory_supervisor',
    version='0.24',
    author="Tim Stahl",
    author_email="tim.stahl@tum.de",
    description="Trajectory Supervisor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=['trajectory_supervisor*']),
    install_requires=['numpy>=1.18.1',
                      'matplotlib>=3.3.1',
                      'scipy>=1.3.3',
                      'trajectory_planning_helpers>=0.75',
                      'scenario_testing_tools>=0.82',
                      'shapely>=1.7.0',
                      'scikit-learn>=0.22.1',
                      'dill>=0.3.3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ])
