import shutil
from setuptools import setup
import distutils.command.check

class TestCommand(distutils.command.check.check):
    """ test command """

    def run(self):

        import doctest

        from MONarchy import MONarchy

        print("======================")
        print("Runs test command ...")

        doctest.testmod(MONarchy)
        print('MONarchy module')

        distutils.command.check.check.run(self)

setup(
    name='MONarchy',
    version='1.0.15',
    description='MON (Meadian of meaNs)',
    maintainer='Samuel DELEPOULLE',
    maintainer_email='samuel.delepoulle@univ-littoral.fr',
    license='MIT',
    packages=['MONarchy'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Utilities'
    ],
    url='https://github.com/prise-3d/MONarchy',
    install_requires=[
        'numpy',
        'pandas',
        'seaborn'
    ],
    cmdclass={
        'test': TestCommand,
    },
    zip_safe=False
)