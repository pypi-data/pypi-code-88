from setuptools import setup

setup(
    version='0.1.0',
    name = 'binrobot',
    description='Bin robot',
    author='cherepanov_max95',
    author_email='cherepanov@ku66.ru',
    install_requires=[
      'aiofile==3.5.1',
      'python-binance==1.0.12',
      'python-dotenv==0.17.1'
    ],
    include_package_data=True,
    zip_safe=False,
    packages=['binrobot']
)