from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "attrs>=19.3",
    "requests>=2.24.0",
    "sqlparse==0.4.1",
    "oddrn>=0.0.4"
]

extras_require = {
    "tests": [
        "pytest",
        "pytest-cov",
        "mock",
        "flake8",
        "SQLAlchemy==1.3.24",       # must be set to 1.3.* for airflow tests compatibility
        "Flask-SQLAlchemy==2.4.4",  # must be set to 2.4.* for airflow tests compatibility
        "pandas-gbq==0.14.1",       # must be set to 0.14.* for airflow tests compatibility
        "apache-airflow==1.10.12",
        "apache-airflow[gcp_api]==1.10.12",
        "apache-airflow[google]==1.10.12",
        "apache-airflow[postgres]==1.10.12",
        "snowflake-connector-python==2.4.3",
    ],
}
extras_require["dev"] = set(sum(extras_require.values(), []))

setup(
    name="odd_airflow",
    version="0.0.5",
    description="ODD adapter to Airflow",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Provectus ODD team",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras_require,
    python_requires=">=3.6",
    zip_safe=False,
    keywords="odd-airflow",
)