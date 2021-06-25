from setuptools import find_packages, setup

setup(
    name='pfibonacci',
    version='1.0.0',
    description="Python starter project",
    url='https://github.com/amnivek/python-fibonacci',
    author='Kevin Ma',
    author_email='zhcnmk@gmail.com',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'fibonacci = fibonacci.bin:compute'
        ]
    }
)
