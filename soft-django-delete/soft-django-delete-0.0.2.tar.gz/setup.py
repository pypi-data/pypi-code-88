from setuptools import setup

setup(
    name='soft-django-delete',
    version='0.0.2',
    packages=['django_soft_delete'],
    url='https://github.com/yucealiosman/soft-delete/',
    license='MIT',
    description='Django Soft Deletion Package',
    long_description='This package provides an abstract django model, '
                     'that allows you to transparently retrieve or '
                     'delete your objects, without having them deleted'
                     ' from your database.',
    install_requires=['django>=2.0.4'],
    author='Ali Osman Yuce',
    author_email='aliosmanyuce@gmail.com',
    classifiers=(
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ),
)
