from setuptools import setup, find_packages


def readme():
    with open("README.rst", "r") as f:
        return f.read()


def requirements():
    with open("requirements.txt", "r") as f:
        return [line.strip() for line in f]


setup(
    name="credit-risk-modelling",
    version="0.0.4",
    description="Tools for Credit Risk Modelling",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=["License :: OSI Approved :: MIT License"],
    keywords="mortgage cashflows annuity interest",
    url="http://github.com/ramonVDAKKER/mortgage_calculus",
    author="Ramon van den Akker",
    author_email="ramon@vandenakker.tech",
    license="MIT",
    packages=find_packages(include=["credit-risk-modelling"]),
    install_requires=requirements(),
    python_requires=">=3.7",
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"],
)
