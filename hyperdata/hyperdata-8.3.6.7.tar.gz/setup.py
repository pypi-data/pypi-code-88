from setuptools import setup, find_packages

setup(
    name="hyperdata",
    version="8.3.6.7",
    description="hyperdata",
    author="hyperdata",
    author_email="mansu_kim@tmax.co.kr",
    url="",
    download_url="",
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=["hyperdata"],
    python_requires=">=3.7",
    package_data={},
    zip_safe=False,
    setup_requires=["pandas>=1.0.1"],
    classifiers=["Programming Language :: Python :: 3.7"],
)
