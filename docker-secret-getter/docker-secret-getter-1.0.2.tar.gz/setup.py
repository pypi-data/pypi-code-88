from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='docker-secret-getter',
    version='1.0.2',
    description='Utility function to fetch docker secrets/envvars. Fork of https://github.com/Fischerfredl/get-docker-secret',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/sajadrahimi/get-docker-secret',
    author='Sajad Rahimi',
    author_email='rahimisajad@outlook.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    keywords=['docker', 'secret', 'envvar', 'config'],
    py_modules=['get_docker_secret'],
    install_requires=[],
    test_suite='tests',
    tests_require=[],
)
