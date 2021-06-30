import setuptools
import converter


with open('README.md') as fr:
    long_description = fr.read()


setuptools.setup(
    name='xlsxCsvConverterrr',
    version=converter.__version__,
    author='Fernatii I.K.',
    author_email='fernatii_ivan@mail.ru',
    description='Сonverting xlsx to csv and vice versa.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Vafernti/MPEI-Project',
    packages=setuptools.find_packages(),
    install_requires=[
        'et-xmlfile>=1.1.0',
        'numpy>=1.21.0',
        'openpyxl>=3.0.7',
        'pandas>=1.2.5',
        'python-dateutil>=2.8.1',
        'pytz>=2021.1',
        'six>=1.16.0'
    ],
    test_suite='tests',
    python_requires='>=3.7',
    platforms=["any"]
)