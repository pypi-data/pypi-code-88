import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django-sap',
    version='1.0.0',
    packages=['sap'],
    description='Integration Sap',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Linets team',
    author_email='avelasqueza@linets.cl',
    url='https://gitlab.com/linets/ecommerce/oms/integrations/oms-sap/',
    license='MIT',
    python_requires=">=3.7",
    install_requires=[
        'Django>=3',
        'requests>=2.25.1'
    ]
)
