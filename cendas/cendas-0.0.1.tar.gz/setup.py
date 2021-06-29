from setuptools import setup

setup(
    name = 'cendas',
    version = '0.0.1',
    description = 'A pandas-based framework optimized for analyzing data provided by the U.S. Census Bureau and other U.S. government agencies.',
    py_modules = ["cendas"],
    package_dir = {'': 'src'},

    install_requires = [
        'pandas'
    ],

    url = 'https://github.com/justinkim668/cendas',
    author = 'Justin Kim',
    author_email = 'jtk2141@columbia.edu'
)
