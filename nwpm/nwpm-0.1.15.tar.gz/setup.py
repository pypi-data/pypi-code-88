from setuptools import setup, find_packages
import sys, os

version = '0.1.15'

setup(name='nwpm',
      version=version,
      description="Navigator Workspace Pack Manager",
      long_description="""\
nwpm is a Workspace Pack Manager for Navigator like npm for node.js""",
      classifiers=[],
      keywords=["nwpm", "navigator", "workspace_pack"],
      author='Alan Hsu',
      author_email='xkevas@qq.com',
      url='https://github.com/xkevas24/nwpm',
      license='Apache-2.0 License',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['pyinstaller'],
      python_requires='>=3.6',
      entry_points={
              'console_scripts': [
                  'nwpm = nwpm.nwpm:__main__'
              ]
          },
      )