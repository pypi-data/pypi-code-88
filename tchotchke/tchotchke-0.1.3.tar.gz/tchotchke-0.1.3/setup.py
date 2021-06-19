from setuptools import setup, find_packages

installation_requirements = [
    "loguru==0.5.3",
    "ujson==4.0.2",
    "pyyaml==5.4.1"
]

setup(
    name="tchotchke",
    description="Trinkets and baubles to adorn your pythonic pursuits.",
    version="0.1.3",
    url="https://github.com/josiahdc/tchotchke",
    author="Josiah Chapman",
    author_email="josiah.chapman@gmail.com",
    packages=find_packages(where="src/*"),
    tests_require=installation_requirements
)
