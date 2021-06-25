from setuptools import setup, find_packages
import pathlib
CWD = pathlib.Path(__file__).parent

README = (CWD / "Readme.md").read_text()

setup(
    name='AgroClient',
    version="1.1.0",
    packages=find_packages(),
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/viswanathbalusu/Agrothon-Client',
    license='AGPL3.0',
    author='viswanathbalusu',
    author_email='ckvbalusu@gmail.com',
    include_package_data=True,
    description='A Client module for Agrothon',
    platforms="any",
    install_requires=[
        "requests==2.25.1",
        "gpiozero==1.5.1",
        "pyserial==3.5",
        "opencv-python==4.5.1.48",
        "RPi.GPIO==0.7.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 5 - Production/Stable"
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts":[
            "AgroClient = agrothon_client.__main__:main"
        ]

    },
)
