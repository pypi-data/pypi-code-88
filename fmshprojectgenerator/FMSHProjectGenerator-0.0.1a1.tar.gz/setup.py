from setuptools import setup, find_packages

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # package information
    name="FMSHProjectGenerator",
    version="0.0.1a1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=['Jinja2>=3.0.1', 'ruamel.yaml>=0.17.9', 'xmltodict>=0.12.0', 'regex>=2021.4.4'],
    package_data={
        'FMSHProjectGenerator': ['assets/*.*', 'chips/*.json'],
        'FMSHProjectGenerator.generators': ['templates/*.*'],
    },
    # metadata for upload to PyPI
    author="Zean Huang",
    author_email="huangzean@fmsh.com.cn",
    description="FMSH(FuDan Microelectronics) general-purpose MCU series IDE project generator",
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/x-rst; charset=UTF-8; variant=GFM",
    # requirements
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ]

)
