from setuptools import setup, find_packages
import sys, os

version = '0.1.19'


with open("README.MD", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(name='nwpm',
      version=version,
      description="Navigator Workspace Pack Manager",
      long_description=long_description,
      long_description_content_type="text/markdown",
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
                  'nwpm = nwpm.nwpm_exec:exec'
              ]
          },
      )