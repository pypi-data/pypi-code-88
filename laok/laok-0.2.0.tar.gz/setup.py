from setuptools import setup, find_packages

setup(
    name='laok',
    version='0.2.0',
    keywords=['_lktest', 'dump_description_help', 'some utils'],
    license='MIT License',
    author='Liu Kuan',
    author_email='1306743659@qq.com',
    description='laok test utils lib',
    packages= find_packages(exclude=("test", "algs"))
)
