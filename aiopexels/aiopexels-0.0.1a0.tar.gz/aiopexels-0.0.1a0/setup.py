import re
from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('aiopexels/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

with open('README.md') as f:
    readme = f.read()

setup(
    name='aiopexels',
    author='scrazzz',
    url='https://github.com/scrazzz/aiopexels',
    project_urls={
        "Documentation": "https://github.com/scrazzz/aiopexels",
        "Issue tracker": "https://github.com/scrazzz/aiopexels/issues"
    },
    version=version,
    license='MIT',
    description='An Asynchronous API wrapper for the Pexels API',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.7.0'
)