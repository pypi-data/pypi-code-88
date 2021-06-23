import setuptools
from os import path

here = path.dirname(path.abspath(__file__))
with open(path.join(here, "README.md"), "r") as readme_file:
    readme = readme_file.read()

with open(path.join(here, "requirements.txt"), "r") as req_file:
    install_requires = req_file.read().splitlines()


setuptools.setup(
    name='ai4ao',
    version='0.1.5',
    decription='Python package for Anomaly Detection and Outlier Detection',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Selvakumar Ulaganathan',
    author_email='flag.selva@gmail.com',
    url='https://gitlab.com/selvai/ai4ao',
    project_urls={
        "Documentation": "https://selvai.gitlab.io/ai4ao/",
        "Developer": "https://www.selvai.com",
    },
    packages=setuptools.find_packages(exclude=('tests', 'docs', 'config', 'data', 'results', 'src')),
    package_data={},
    include_package_data=False,
    python_requires='>=3.6',
    install_requires=install_requires,
    keywords=['Anomaly Detection', 'Outlier Detection'],
    classifiers=["Topic :: Scientific/Engineering :: Artificial Intelligence"]
)
