# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call


class InstallPluginCommand(install):
    def run(self):
        install.run(self)
        try:
            check_call(['pulumi', 'plugin', 'install', 'resource', 'gcp-scaffold', '0.1.1-alpha.1624185341+66dd259b'])
        except OSError as error:
            if error.errno == errno.ENOENT:
                print("""
                There was an error installing the gcp-scaffold resource provider plugin.
                It looks like `pulumi` is not installed on your system.
                Please visit https://pulumi.com/ to install the Pulumi CLI.
                You may try manually installing the plugin by running
                `pulumi plugin install resource gcp-scaffold 0.1.1-alpha.1624185341+66dd259b`
                """)
            else:
                raise


def readme():
    try:
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
            return "gcp-scaffold Pulumi Package - Development Version"


setup(name='cobraz_pulumi_gcp_scaffold',
      version='0.1.1a1624185341',
      long_description=readme(),
      long_description_content_type='text/markdown',
      cmdclass={
          'install': InstallPluginCommand,
      },
      packages=find_packages(),
      package_data={
          'cobraz_pulumi_gcp_scaffold': [
              'py.typed',
          ]
      },
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=3.0.0,<4.0.0',
          'pulumi-gcp>=5.0.0,<6.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)
